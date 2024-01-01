import dash
from dash import dcc, html, Input, Output, State
import base64
import io
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import cv2
import dash_bootstrap_components as dbc
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('./visualization/keras_100pochs_data_augmentation=Trueopt=Adam.h5')

# Define class names
class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck', 'Fish', 'Flowers', 'Trees']

# Create the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

# Define app layout using Dash Bootstrap Components
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Image Classification App", style={'text-align': 'center', 'margin-top': '20px'}))
    ]),
    dbc.Row([
        dbc.Col(dcc.Upload(
            id='upload-image',
            children=html.Div([
                html.H3('Drag and Drop or Click to Select an Image', style={'margin': '20px'}),
            ]),
            style={
                'width': '50%',
                'height': '200px',
                'lineHeight': '200px',
                'borderWidth': '2px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '20px auto',
                'background-color': '#F0F0F0',
                'color': '#444',
                'font-size': '18px',
                'font-weight': 'bold',
            },
            multiple=False
        ))
    ]),
    dbc.Row([
        dbc.Col(html.H1("Webcam Image Capture"))
    ]),
    dbc.Row([
        dbc.Col(html.Img(id='captured-image', style={'width': '0%', 'border': '2px solid #333'}))
    ]),
    dbc.Row([
        dbc.Col(html.Button('Open Camera', id='open-camera-button', n_clicks=0, style={'margin': '10px'})),
        dbc.Col(html.Button('Capture Image', id='capture-button', n_clicks=0, style={'margin': '10px'})),
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output-image', style={'text-align': 'center', 'margin': '20px'}))
    ])
])

# Global variable to store the camera instance
camera = None

def open_camera():
    global camera
    cap = cv2.VideoCapture(1)  # Use '0' for the default camera (typically webcam)
    camera = cap
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        # Break the loop when the 'Capture Image' button is clicked
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    return frame

@app.callback(
    Output('captured-image', 'src'),
    Input('open-camera-button', 'n_clicks'),
    Input('capture-button', 'n_clicks'),
    prevent_initial_call=True
)
def update_image(n_clicks_open, n_clicks_capture):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update

    if 'open-camera-button' in ctx.triggered[0]['prop_id']:
        if n_clicks_open > 0:
            # Open the camera when the 'Open Camera' button is clicked
            open_camera()
            return dash.no_update

    elif 'capture-button' in ctx.triggered[0]['prop_id']:
        if n_clicks_capture > 0:
            if camera is not None:
                # Capture the image when the 'Capture Image' button is clicked
                ret, frame = camera.read()
                camera.release()
                cv2.destroyAllWindows()
                # Convert the captured frame to JPEG format
                _, buffer = cv2.imencode('.jpg', frame)
                # Convert the buffer to base64 encoded string
                image_base64 = base64.b64encode(buffer).decode('utf-8')
                # Create an 'Img' component with the captured image as the 'src'
                captured_image = f"data:image/jpg;base64,{image_base64}"
                return captured_image

    return 'assets/placeholder.png'

# Preprocess the uploaded image and make predictions


def down_sampling(image_content):
    # Convert the image content (bytes) to a PIL Image object
    image = Image.open(io.BytesIO(image_content))
    
    # Resize the image to the desired size (32x32) using Lanczos interpolation
    resized_image = image.resize((32, 32), Image.LANCZOS)
    
    # Convert the resized image back to bytes
    resized_content = io.BytesIO()
    resized_image.save(resized_content, format='JPEG')
    
    return resized_content.getvalue()


def preprocess_image(image_content):
    # img /= 255
    # image_content=down_sampling(image_content)
    img = load_img(io.BytesIO(image_content), target_size=(32, 32))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    return img

def predict(image_content):
    img = preprocess_image(image_content)
    prediction = model.predict(img)[0]
    predicted_class = np.argmax(prediction)
    confidence = prediction[predicted_class]
    return class_names[predicted_class], confidence

# Define the update_output function to handle image predictions
def update_output(contents, filename=""):
    if contents is not None:
        children = [
            html.Img(src=contents, style={'width': '20%', 'border': '2px solid #333', 'margin': '20px'}),
            html.Hr(),
            html.H3(f'Prediction for {filename}:'),
        ]
        class_name, confidence = predict(base64.b64decode(contents.split(',')[1]))
        children.append(html.H4(f'Class: {class_name} | Confidence: {confidence:.2f}', style={'margin-bottom': '20px'}))
        return children
    else:
        return html.Div()

# Callback to update the output
@app.callback(Output('output-image', 'children'),
              Input('upload-image', 'contents'),
              Input('captured-image', 'src'),
              State('upload-image', 'filename'))
def update(contents, src, filename=""):
    ctx = dash.callback_context

    if not ctx.triggered:
        return dash.no_update

    if 'upload-image' in ctx.triggered[0]['prop_id']:
        # Handle the case when an image is uploaded
        return update_output(contents, filename)
    elif 'captured-image' in ctx.triggered[0]['prop_id']:
        # Handle the case when an image is captured from the webcam
        return update_output(src, "Webcam Captured Image")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
