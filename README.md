# Gamma Ray Data Extraction Tool

## Overview
This project provides a Tkinter-based GUI tool for processing gamma ray images and extracting data points based on color detection. The extracted data points are scaled, adjusted, and exported to a CSV file. This tool is useful for applications requiring gamma ray feature extraction and data transformation from images.

**Code:** [`Gamma Ray Detection`](https://github.com/MohdIllham/Gamma-Ray-Detection/blob/main/Gamma%20Ray%20Detection.py)

## Table of Contents
- [Overview](#Overview)
- [Features](#Features)
- [Dependencies](#Dependencies)
- [Usage](#Usage)
- [GUI Components)](#GUI-Components)
- [Functions](#Functions)

## Features
- Image Browsing: Select a gamma ray image file to process.
- Output Path Selection: Choose a location to save the output CSV file.
- Red Color Detection: Detect red color regions in the image using HSV color space.
- Scaling and Adjustment: Scale the detected data points and adjust them to a minimum Y-coordinate.
- CSV Export: Save the processed data points to a CSV file.

## Dependencies
- Python 3.x
- NumPy
- OpenCV
- Tkinter

You can install the required libraries using:
```
pip install requests pandas numpy yfinance matplotlib seaborn scikit-learn
```

## Installation 
To run the project, you need the following Python libraries:

```
pip install numpy opencv-python tk
```
## Usage

1. Run the Script:
  ```
  python Gamma Ray Detection.py

  ```
2. Input Parameters:

  - Enter the scale factor for x-coordinates.
  - Enter the scale factor for y-coordinates.
  - Enter the minimum Y-coordinate for adjustment.

3. Browse and Select Image:
  - Click the "Browse Image" button to select a gamma ray image file.

4. Select Output Path:

  - Click the "Select Output Path" button to choose the location for saving the CSV file.

5. Run the Script:
  - Click the "Run" button to process the image, extract data points, and save them to the CSV file.



## GUI Components
  - Labels and Entries: For scale factors and minimum Y-coordinate input.
  - Buttons: For browsing images, selecting output path, and running the script.
  - Labels: To display the selected image and output file paths

## Functions
  - validate_number: Validates the input for scale factors and minimum Y-coordinate to ensure they are integers or floats
  - process_image: Loads the image, detects red regions, scales and adjusts the data points, and exports them to a CSV file.
  - browse_image: Opens a file dialog to browse and select an image file.
  - select_output_path: Opens a file dialog to choose the output CSV file location.
  - run_script: Validates inputs, converts them to appropriate types, and calls process_image to execute the main functionality.
  - Example :
        ```
        1. Enter scale factor x: 0.5
        2. Enter scale factor y: 0.5
        3. Enter min-Y coordinate: 100
        4. Browse and select a gamma ray image file.
        5. Select the output path for the CSV file.
        6. Click "Run" to process the image and save the data points.
       ```



