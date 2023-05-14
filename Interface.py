import tkinter as tk
from tkinter import filedialog
import time
from parkinson_model import predictionTester, train
from PIL import ImageTk, Image
import shutil
import os 

root = tk.Tk()
root.title("Parkinson's Detection")
root.geometry("650x900")
root.resizable(False, False)
# Function to show a loading screen
def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.geometry("100x50")
    loading_label = tk.Label(loading_screen, text="Loading...")
    loading_label.pack()
    loading_screen.update()  # Force the loading screen to update

    # Simulate loading for 3 seconds
    time.sleep(3)

    # Close the loading screen after loading is done
    loading_screen.destroy()

# Function to handle image selection
def browse_file():
    global choice_var
    global file_path
    file_path = filedialog.askopenfilename()
    result = predictionTester(train("spiral"), file_path)
    show_loading_screen()
    temp = " may have Parkinsons" if result[0] else " may be Healthy"
    output_label['text'] = "Result: We predict that you" + temp
    output_label['fg'] = "red" if result[0] else 'green'
    survey_label['text'] = "Do you know if you actually have Parkinson's? Your answer will help improve our model." + "\n Select \"Unsure\" if you do not wish to upload your image to the database."
    # Add multiple choice buttons
    choice_frame = tk.Frame(root)
    choice_frame.place(relx = 0.5, rely = 0.8, anchor = 'center')
    choice_var = tk.StringVar()
    yes_button = tk.Radiobutton(choice_frame, text="I have Parkinson's", variable=choice_var, value="Yes")
    yes_button.pack(side=tk.LEFT)
    no_button = tk.Radiobutton(choice_frame, text="I am Healthy", variable=choice_var, value="No")
    no_button.pack(side=tk.LEFT)
    unsure_button = tk.Radiobutton(choice_frame, text="Unsure", variable=choice_var, value="Unsure")
    unsure_button.pack(side=tk.LEFT)

    done_button = tk.Button(root, text="Upload Image to Database/Continue", command=save_image)
    done_button.place(relx=0.5, rely=0.9, anchor="center")

def save_image():
    if choice_var.get() == "Yes":
        shutil.copy2(file_path, "/Users/erikli/Desktop/Hackathon/Parkinson/data/drawings/spiral/training/parkinson")
        output_label['text'] = f"Image saved to Unhealthy training data (you may safely exit)"
        output_label['fg'] = "light blue"
    elif choice_var.get() == "No":
        folder_name = "healthy" 
        shutil.copy2(file_path, "/Users/erikli/Desktop/Hackathon/Parkinson/data/drawings/spiral/training/healthy")
        output_label['text'] = f"Image saved to Healthy training data (you may safely exit)"
        output_label['fg'] = "light blue"
    else:
        output_label['text'] = f"You may safely exit"
        output_label['fg'] = "light blue"
# Create the image selection button
browse_button = tk.Button(root, text="Select Image", command = browse_file)
browse_button.place(relx = 0.5, rely = 0.9, anchor = "center")

#Default Image
guide_image = ImageTk.PhotoImage(Image.open("/Users/erikli/Desktop/Parkinson Test Drawings/guide.png"))
panel = tk.Label(root, image = guide_image)
panel.place(relx = 0.5, rely = 0.4, anchor = "center")

#Description at top
description = tk.Label(root, text = "Draw this image by hand (excluding axes) as best as you can, \n then upload image using the \"Select Image\" button below.")
description.place(relx = 0.5, rely = 0.1, anchor = 'center')
description.config(font = ("Helvetica", 15))

output_label = tk.Label(root)
output_label.place(relx = 0.5, rely = 0.65, anchor = 'center')
output_label.config(font = ("Helvetica", 18))

survey_label = tk.Label(root)
survey_label.place(relx = 0.5, rely = 0.725, anchor = 'center')

root.mainloop()
