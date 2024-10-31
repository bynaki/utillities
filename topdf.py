from PIL import Image
import os

# 이미지 파일들이 있는 폴더 경로를 지정하세요
image_dir = './images'  # 여기를 실제 폴더 경로로 변경하세요

# 지원하는 이미지 파일 확장자 목록
image_extensions = ('.jpeg', '.jpg', '.png', '.bmp', '.gif', '.tiff')

# 폴더 내의 모든 이미지 파일 목록을 가져옵니다
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)]

# 파일들을 생성된 순서대로 정렬합니다
image_files.sort(key=lambda x: os.path.getctime(os.path.join(image_dir, x)))

# DPI 설정
desired_dpi = (300, 300)

# 이미지들을 열고 RGB 모드로 변환합니다
images = []
for file in image_files:
    img_path = os.path.join(image_dir, file)
    try:
        img = Image.open(img_path).convert('RGB')
        images.append(img)
    except Exception as e:
        print(f"{file}을(를) 열 수 없습니다: {e}")

# 모든 이미지를 하나의 PDF 파일로 저장합니다
if images:
    output_path = 'output.pdf'  # 현재 디렉토리에 저장
    images[0].save(output_path, save_all=True, append_images=images[1:], dpi=desired_dpi)
    print(f"PDF 파일이 성공적으로 저장되었습니다: {output_path}")
else:
    print("폴더에 변환할 수 있는 이미지 파일이 없습니다.")