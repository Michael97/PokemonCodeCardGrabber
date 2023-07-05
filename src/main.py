from PIL import Image
import pytesseract
from pyzbar.pyzbar import decode
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Michael/AppData/Local/Programs/Tesseract-OCR/tesseract.exe' # replace this with your own path.
import os
import logging
import shutil
import glob

# Set up logging
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

failed_images_path = f'{os.getcwd()}/failed_images'
completed_image_path = f'{os.getcwd()}/completed_images'

images_folder = f'{os.getcwd()}/images'

image_files = glob.glob(f"{images_folder}/*.*")

for image_file in image_files:
    try:
        # Step 1: Load Image
        img = cv2.imread(image_file)
        clean_img = cv2.medianBlur(img, 5)

        # Step 2: Detect QR Code
        decoded_objects = decode(clean_img)
        if not decoded_objects:
            logging.info(f'No QR code found in {image_file}')
            shutil.move(image_file, f'{failed_images_path}/{os.path.basename(image_file)}')  # Move to failed images folder
            continue

        for obj in decoded_objects:
            logging.info('Type: ' + obj.type)
            qr_data = obj.data.decode('utf-8')
            logging.info('Data: ' + qr_data)

        # Cut out bottom right part of the card to get set name and code
        height, width, _ = clean_img.shape
        start_row, start_col = int(height * .47), int(width * .375)
        set_name_roi = clean_img[start_row:, start_col:]
        #cv2.imwrite(f'{os.getcwd()}/setnameimage.jpg', set_name_roi) #Uncomment to see what part of the image we're cutting

        # Perform OCR on the set name region of interest (ROI)
        ocr_result = pytesseract.image_to_string(set_name_roi)

        # Split the result into lines, ignoring lines shorter than 4 characters or starting with 'EN'
        lines = [line.strip() for line in ocr_result.split('\n') if line.strip() != '' and len(line) > 4 and not line.startswith('EN')]

        logging.info(f'Extracted data - {lines}')

        if len(lines) < 2:
            logging.info(f'Failed to extract code and set name from {image_file}')
            shutil.move(image_file, f'{failed_images_path}/{os.path.basename(image_file)}')  # Move to failed images folder
            continue

        # The first non-empty line should be the code and the second non-empty line should be the set name
        code = lines[0]  # The first non-empty line
        set_name = lines[1]  # The second non-empty line

        logging.info(f'Extracted code: "{code}"')
        logging.info(f'Extracted set name: "{set_name}"')

        if code != qr_data:
            logging.info(f'Code from OCR does not match QR code data in {image_file}')
            shutil.move(image_file, f'{failed_images_path}/{os.path.basename(image_file)}')  # Move to failed images folder
            continue

        # If the code matches, write to the file
        logging.info('Codes match. Writing to file...')
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(f'{code},{set_name}\n')

        shutil.move(image_file, f'{completed_image_path}/{os.path.basename(image_file)}')  # Move to failed images folder

    except Exception as e:
        logging.error(f'An error occurred processing {image_file}: {e}')
        shutil.move(image_file,  f'{failed_images_path}/{os.path.basename(image_file)}')  # Move to failed images folder
