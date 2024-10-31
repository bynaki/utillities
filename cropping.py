import os
import re
from PIL import Image # type: ignore
import img2pdf # type: ignore


# Configure
#
# 이미지 파일이 저장된 디렉토리
image_dir = "/Users/naki/Documents/images"
# 결과 pdf 파일명
output_pdf = "output.pdf"
# 이미지 접두사
# 예: image_0001.png 에서 image_
prefix = "image_"
# Define the region to crop (left, upper, right, lower)
# 홀수 페이지
odd_region = (100, 90, 1300, 2220)
# Define the region to crop (left, upper, right, lower)
# 짝수 페이지
even_region = (140, 90, 1340, 2220)
# dpi를 맞추자
dpix = dpiy = 300


# 임시 폴더 생성
temp_dir = os.path.join(image_dir, "temp_images")
os.makedirs(temp_dir, exist_ok=True)

files_and_dirs = os.listdir(image_dir)
files = [f for f in files_and_dirs if os.path.isfile(os.path.join(image_dir, f))]
files.sort()

pattern = f"({prefix})(\\d+)"

temp_images = []
# 이미지를 잘라내어 임시 폴더에 저장
for file in files:
    filename, extention = os.path.splitext(file)
    match = re.match(pattern, filename)
    if match:
        image = Image.open(os.path.join(image_dir, file))
        num = int(match.groups()[1])
        if num % 2 == 0:
            cropped_image = image.crop(even_region)
        else:
            cropped_image = image.crop(odd_region)
        temp_img_path = os.path.join(temp_dir, file)
        cropped_image.save(temp_img_path)
        temp_images.append(temp_img_path)
        print(f"cropped > {file}")

print("saving...")
# 이미지를 dpi 크기에 맞추어 pdf로 변환하여 저장
layout_fun = img2pdf.get_fixed_dpi_layout_fun((dpix, dpiy))
with open(output_pdf, 'wb') as f:
    f.write(img2pdf.convert(temp_images, layout_fun=layout_fun))
import shutil
shutil.rmtree(temp_dir)
print(f"saved to {output_pdf}")
