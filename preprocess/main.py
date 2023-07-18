import cifar100
import cifr10_reed_save
import cifr10_creat_csv_label_path

from our_data_creat_csv import create
from our_data_down_sampling import downsampling
from our_data_save_as_numpy import save_as_numpy
from normalization import normalization
#our data
create()
images = downsampling()
save_as_numpy(images)
normalization()
#merge
#train and test
