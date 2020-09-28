import os
import shutil
import zipfile
import tempfile
import argparse
import logging

logging.basicConfig(filename="files.log", format="%(asctime)s -- %(message)s", level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("-f", help="zip file for analyze", required=True)
args = parser.parse_args()
zip_file = args.f

with tempfile.TemporaryDirectory() as tmpdir:
    with zipfile.ZipFile(zip_file, "r") as zf:
        zf.extractall(path=tmpdir)

    itmpdir = tmpdir + "/" + zip_file[:-4]
    for dirpath, dirnames, files in os.walk(itmpdir):
        flag = True
        for file_name in files:
            if file_name == "__init__.py":
                flag = False
        if flag:
            logging.info(f"'{dirpath}' has been removed")
            shutil.rmtree(dirpath)

    shutil.copytree(itmpdir, "./ans/")

    new_zip = zip_file[:-4] + "_new.zip"
    with zipfile.ZipFile(new_zip, "w") as zf:
        for dirpath, dirnames, files in os.walk("./ans/"):
            zf.write(dirpath)
            for filename in files:
                zf.write(os.path.join(dirpath, filename))
