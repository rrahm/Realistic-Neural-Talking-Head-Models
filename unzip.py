import zipfile

with zipfile.ZipFile("vox2_dev_mp4aa.zip","r") as zip_ref:
    zip_ref.extractall("/content")