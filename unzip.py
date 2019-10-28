import zipfile

with zipfile.ZipFile("/content/drive/My Drive/mp4vox2_dev_mp4aa.zip","r") as zip_ref:
    zip_ref.extractall("/content")