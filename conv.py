import pathlib

import pdf2image

# sudo apt-get install poppler-utils
pdf_files = pathlib.Path("data_pdf").glob("*.pdf")
img_dir = pathlib.Path("data_img")

for pdf_file in pdf_files:
    base = pdf_file.stem
    images = pdf2image.convert_from_path(pdf_file, grayscale=True, size=640)
    for index, image in enumerate(images):
        image.save(img_dir / pathlib.Path(base + "-{}.png".format(index + 1)), "png")
