# AI Image Generator

AI Image Generator is a Python application that utilizes OpenAI's GPT-3 to generate images based on user prompts and style preferences. This application provides a graphical user interface (GUI) built using Tkinter for a seamless user experience.

## Features

- Generate images from textual prompts.
- Choose from different art styles such as Realistic, Cartoon, 3D Illustration, and Flat Art.
- Control the number of images generated with a slider.
- Display the generated images directly in the GUI.

## Requirements

- Python 3.x
- `customtkinter` library (Install with `pip install customtkinter`)
- `openai` library (Install with `pip install openai`)
- `PIL` library (Install with `pip install Pillow`)
- `requests` library (Install with `pip install requests`)

## Usage

1. Set up your OpenAI API key.

2. Run the `main.py` script to launch the application.

3. Enter a prompt in the "Prompt" text box.

4. Select a style from the "Style" dropdown menu.

5. Adjust the number of images to generate using the slider.

6. Click the "Generate" button to create and display the images.

## Customization

- You can further customize the GUI's appearance and layout by modifying the code in `main.py`.
- Adjust the initial window size by changing the `root.geometry` line.


## Acknowledgments

- [OpenAI](https://openai.com) for their powerful GPT-3 model.
- [customtkinter](https://pypi.org/project/customtkinter/) for enhanced Tkinter widgets.

