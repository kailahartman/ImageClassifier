from cfar10.cfar10_main import cfar10_read_save_locally_numpy_csv
from cfar100.cfar100_main import cfar100_read_save_locally_numpy_csv
from our_data_creat_csv import create
from our_data_down_sampling import downsampling
from our_data_save_as_numpy import save_as_numpy
from normalization import normalization
cfar10_read_save_locally_numpy_csv()
cfar100_read_save_locally_numpy_csv()
create()
images = downsampling()
save_as_numpy(images)
normalization()
#merge
#train and test