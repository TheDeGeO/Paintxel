# PaintXel

A modern, lightweight pixel art editor built with Python and Pygame. PaintXel provides a simple and intuitive interface for creating, editing, and saving pixel art designs.

![PaintXel](https://img.shields.io/badge/PaintXel-Pixel%20Art%20Editor-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green)

## Features

- **Simple Interface**: User-friendly UI designed for both beginners and experienced pixel artists
- **Multiple Tools**: Draw, erase, zoom, rotate, and reflect your pixel art
- **Color Palette**: Pre-defined pastel colors with easy selection
- **File Management**: Save and load your pixel art projects
- **Export Options**: Export your art as ASCII text
- **View Modes**: High contrast and negative view modes for different perspectives

## Screenshots

<!-- 
Add your application screenshots here, for example:
![Screenshot of PaintXel](path/to/screenshot.png)
-->

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/Paintxel.git
   cd Paintxel
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Start the application by running:

```
python main.py
```

### Main Controls

- **Left Panel**: Tool selection and color palette
- **Center Area**: Canvas for pixel art creation
- **Right Panel**: Special view modes and export options

### Tools

- **Draw** (󰛿): Paint pixels on the canvas
- **Erase** (󰇾): Remove pixels from the canvas
- **Zoom** (): Magnify the view of pixels
- **Rotate** (): Rotate the entire canvas clockwise or counterclockwise
- **Reflect** (󰨏,󰨎): Flip the canvas vertically or horizontally
- **Save** (󰆓): Save your pixel art to a file
- **Reload** (): Reload the canvas from a saved file
- **Clear** (): Clear the entire canvas
- **Quit** (): Return to the title screen

### Special Functions

- **High Contrast** (󰆗): View your art with enhanced contrast
- **Negative** (󰌁): View the negative (inverted colors) of your art
- **ASCII View** (󱔁󰈈): View your pixel art converted to ASCII characters
- **Save ASCII** (󱔁): Export your pixel art as an ASCII text file

## Project Structure

- `main.py`: Main application entry point
- `screenTypes.py`: Screen and UI layout definitions
- `guiTools.py`: GUI components and canvas functionality
- `fileManager.py`: File saving and loading utilities
- `colors.py`: Color palette definitions
- `assets/`: Fonts and other resources
- `saves/`: Directory for saved pixel art files
- `DOCS/`: Additional documentation

## Dependencies

- Python 3.x
- Pygame 2.6.1
- Tkinter (included in standard Python)

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Pygame](https://www.pygame.org/) game development library
- [Nerd Fonts](https://www.nerdfonts.com/) Inconsolata font used in the UI 