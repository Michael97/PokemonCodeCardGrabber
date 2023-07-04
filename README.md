# Pokemon Code Card Grabber :dragon: :camera:

Welcome to the Pokemon Code Card Grabber project! This Python project helps you to process images of Pokemon code cards, extract the code, and the name of the pack, then output the data to a text file. :zap: :computer:

## Prerequisites 📑

You must have Python 3.8 installed globally on your system.

Additionally, Tesseract must be installed on your system. You can head to the [official Tesseract repository](https://github.com/tesseract-ocr/tesseract#installing-tesseract) and follow the steps provided there for installation. Make sure you install the version compatible with your system's architecture.

## Installation :gear:

1. Clone this repository to your local machine.

```
git clone https://github.com/Michael97/pokemoncodegrabber.git
```

2. Navigate to the project directory.
```
cd pokemoncodegrabber
```
3. Create a virtual environment.
```
python -m venv venv
```
4. Activate the virtual environment.
```
source venv/bin/activate # Linux or macOS
```
```
.\venv\Scripts\activate # Windows
```

5. Install the required packages.
```
pip install -r requirements.txt
```

## Usage :computer:

Pop your code card images into the "images" folder and then run the following in cmd;

```python
python main.py
```

The program will process each image, extract the code and the name of the pack, and log this information to an 'output.txt' file.

Any images that fail to be processed will be moved to the 'failed_images' folder. If you encounter any difficulties, consult the 'logs.txt' file for more detailed error reports.

## Contributing :busts_in_silhouette:
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. :bulb:

## License :page_with_curl:
MIT
