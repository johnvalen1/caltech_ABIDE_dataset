import matplotlib.pyplot as plt
import nibabel as nib
import os
from PIL import Image

universal_img_name = 'mprage.nii'

control_patients_dir = ".\\control\\"
treatment_patients_dir = ".\\treatment\\"

CONTROL_JPEGS_DIR = ".\\JPEGimages\\control\\"
TREATMENT_JPEGS_DIR = ".\\JPEGimages\\treatment\\"

SLICE_NUM = 120

def extract_slice(nii_image_path, class_name, slice_number = SLICE_NUM):
    """
    Read in an .nii image, convert it to a numpy ndarray. Return the array and its file name.
    """
    nii_img = nib.load(nii_image_path).get_fdata()
    slice = nii_img[ :, :, slice_number]
    if class_name == "control":
        slice_name = nii_image_path[10:17]
    if class_name == "treatment":
        slice_name = nii_image_path[12:19]
    return slice, slice_name

def nii_to_jpeg(nii_slice, slice_name, save_dir):
    """
    Save the ndarray representation of the nii image to JPEG format, named according to its original name.
    """
    im = Image.fromarray(nii_slice)
    im = im.convert("L")
    print(save_dir + slice_name + ".jpeg")
    im.save(save_dir + slice_name + ".jpeg")

if __name__ == '__main__':
    # Check whether the specified path exists or not
    controlDirectoryExists = os.path.exists(CONTROL_JPEGS_DIR)
    if not controlDirectoryExists:
        # Create a new directory because it does not exist
        os.makedirs(CONTROL_JPEGS_DIR)
        print("The new CONTROL JPEGs directory is created!")

    treatmentDirectoryExists = os.path.exists(TREATMENT_JPEGS_DIR)
    if not treatmentDirectoryExists:
        # Create a new directory because it does not exist
        os.makedirs(TREATMENT_JPEGS_DIR)
        print("The new TREATMENT JPEGs directory is created!")

    # populate the control directory with JPEG representations
    for nii_image_path in os.listdir(control_patients_dir):
        nii_image_path = "{}{}\\{}".format(control_patients_dir, nii_image_path, universal_img_name)
        extracted_slice, extracted_slice_name = extract_slice(nii_image_path, class_name="control")
        nii_to_jpeg(extracted_slice, extracted_slice_name, save_dir = CONTROL_JPEGS_DIR)

    # populate the treatment directory with JPEG representations
    for nii_image_path in os.listdir(treatment_patients_dir):
        nii_image_path = "{}{}\\{}".format(treatment_patients_dir, nii_image_path, universal_img_name)
        extracted_slice, extracted_slice_name = extract_slice(nii_image_path, class_name="treatment")
        nii_to_jpeg(extracted_slice, extracted_slice_name, save_dir = TREATMENT_JPEGS_DIR)



