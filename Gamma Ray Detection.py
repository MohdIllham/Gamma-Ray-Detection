
import numpy as np
import cv2
import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def validate_number(input_val):
    try:
        float_val = float(input_val)
        
        # Check if the float has more than 2 decimal places
        if float_val != round(float_val, 2):
            raise ValueError
        return True
    except ValueError:
        try:
            int_val = int(input_val)
            return True
        except ValueError:
            return False

def process_image(scale_x, scale_y, min_y_coordinate, image_path_var, output_path_var, root):
    image_path = image_path_var.get()  # Get the selected image path
    # Load the Image
    img = cv2.imread(image_path)

    # Convert to HSV for color detection
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range for detecting red color
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for both ranges and combine them
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Define the scale factors
    scale_factor_x = scale_x
    scale_factor_y = scale_y

    data_points = []
    for contour in contours:
        for point in contour:
            x, y = point[0]
            # Apply scale factor
            scaled_x = x * scale_factor_x
            scaled_y = y * scale_factor_y
            data_points.append((scaled_x, scaled_y))

    # Calculate the minimum x and y values
    x_coords, y_coords = zip(*data_points)
    xmin = min(x_coords)
    ymin = min(y_coords)

    # Adjust coordinates to set the min-Y coordinate
    adjusted_data_points = [(x, min_y_coordinate - (y - ymin)) for x, y in data_points]

    print("Extracted data points:")
    for x, y in adjusted_data_points:
        print(f"x: {x}, y: {y}")

    # Ask the user to select the CSV output file location
    csv_file_path = output_path_var.get()
    if not csv_file_path:
        csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not csv_file_path:
            return  # User cancelled the file dialog
    
    # Update the output file path variable
    output_path_var.set(csv_file_path)

    # Export data points to the CSV file
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Writing the header
        writer.writerows(adjusted_data_points)

    print(f"Data points have been exported to {csv_file_path}")

    # Close the Tkinter window
    root.destroy()

def browse_image(image_path_var):
    image_path = filedialog.askopenfilename()  # Get the path of the selected file
    # Update the label with the selected image path
    image_path_var.set(image_path)

def select_output_path(output_path_var):
    # Ask the user to select the output file location
    csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        output_path_var.set(csv_file_path)

def run_script(scale_x_entry, scale_y_entry, min_y_entry, image_path_var, output_path_var, root):
    scale_x = scale_x_entry.get()
    scale_y = scale_y_entry.get()
    min_y_coordinate = min_y_entry.get()

    # Validate input values
    if not validate_number(scale_x):
        messagebox.showerror("Error", "Scale factor x must be a float or integer.")
        return
    if not validate_number(scale_y):
        messagebox.showerror("Error", "Scale factor y must be a float or integer.")
        return
    if not validate_number(min_y_coordinate):
        messagebox.showerror("Error", "Min-Y coordinate must be a float or integer.")
        return

    # Convert validated input values to float
    scale_x = float(scale_x)
    scale_y = float(scale_y)
    min_y_coordinate = float(min_y_coordinate)
    
    process_image(scale_x, scale_y, min_y_coordinate, image_path_var, output_path_var, root)

# Create a Tkinter window
root = tk.Tk()
root.title("Scale Input")

# StringVar to store the selected image path
image_path_var = tk.StringVar()

# StringVar to store the selected output file path
output_path_var = tk.StringVar()

# Label and Entry for scale factor x
scale_x_label = tk.Label(root, text="Enter scale factor x:")
scale_x_label.grid(row=0, column=0)
scale_x_entry = tk.Entry(root)
scale_x_entry.grid(row=0, column=1)

# Label and Entry for scale factor y
scale_y_label = tk.Label(root, text="Enter scale factor y:")
scale_y_label.grid(row=1, column=0)
scale_y_entry = tk.Entry(root)
scale_y_entry.grid(row=1, column=1)

# Label and Entry for min-Y coordinate
min_y_label = tk.Label(root, text="Enter min-Y coordinate:")
min_y_label.grid(row=2, column=0)
min_y_entry = tk.Entry(root)
min_y_entry.grid(row=2, column=1)

# Button to browse image
browse_button = tk.Button(root, text="Browse Image", command=lambda: browse_image(image_path_var))
browse_button.grid(row=3, column=0)

# Button to select output path
select_output_button = tk.Button(root, text="Select Output Path", command=lambda: select_output_path(output_path_var))
select_output_button.grid(row=3, column=1)

# Label to display selected image path
image_path_label = tk.Label(root, textvariable=image_path_var)
image_path_label.grid(row=4, columnspan=2)

# Label to display selected output file path
output_path_label = tk.Label(root, textvariable=output_path_var)
output_path_label.grid(row=5, columnspan=2)

# Button to run script
run_button = tk.Button(root, text="Run", command=lambda: run_script(scale_x_entry, scale_y_entry, min_y_entry, image_path_var, output_path_var, root))
run_button.grid(row=6, columnspan=2)

# Start the Tkinter event loop
root.mainloop()


# %%
