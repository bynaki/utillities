# Utillities

### cropping.py
> 이미지 문서를 자르고 pdf로 변환 ocr을 더하여

```shell
pip install img2pdf  # 이미지를 pdf로 변환 라이브러리
python cropping.py
brew install ocrmypdf  # OCRmyPDF adds an OCR text layer to scanned PDF files
brew install tesseract-lang  # language packs
ocrmypdf -l kor+eng input.pdf output-ocr.pdf
```

### topdf.py
> 이미지들을 생성된 순서로 정렬하고 pdf로 변환

```shell
python topdf.py
```