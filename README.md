# Pokemon Code Card Grabber :dragon: :camera:

Welcome to the Pokemon Code Grabber project! This Python project helps you to take images of Pokemon code cards, extract the QR code, code, and name of the pack. :zap: :computer:

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

Replace `<image_path>` with the path to the image file that you want to process.

```python
python main.py <image_path>
```

The program will save a new image with the QR code highlighted, and it will print the extracted information to the console.

## Contributing :busts_in_silhouette:
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. :bulb:

## License :page_with_curl:
MIT
