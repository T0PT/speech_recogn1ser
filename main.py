import tkinter as tk
from tkinter import filedialog
import os
import shutil

import converter 
import whisper_api as whisper

input_filetypes=[("All files", "*.*"), ("Audio m4a", "*.m4a"),
                   ("Audio wav", "*.wav"), ("Audio mp3", "*.mp3"),
                    ("Audio flac", "*.flac"), ("Video mkv", "*.mkv"),
                    ("Video mp4", "*.mp4")]

available_extensions = ["wav", "mp3", "flac", "mkv"]

project_dir = os.getcwd()
project_dir = project_dir.replace("\\", "/")

filename = ""
origname = ""
extension = ""
status = False

available_models = ["tiny", "small", "base", "medium"]

def select_file():
    global filename, extension, status, origname
    filename = filedialog.askopenfilename(
        title="Select a file",
        filetypes=input_filetypes,
    )
    # You can access the selected file path in the 'filename' variable
    if filename:
        origname = filename
        filename = rename_with_underscore(filename)
        extension = filename.split('.')[-1]
        # filename = filename.replace("\", "/")
        pretty_filename = filename.split('/')[-1]
        update_label2(pretty_filename)
        if extension not in available_extensions:
            update_status("Not available file type ❌")
            status = False
        else:
            update_status("Ready")
            status = True
        print(filename)  # Or perform any action with the file path

def update_label2(filename):
    label2.config(text=f"Selected File: {filename}")

def update_status(status):
    status_label.config(text=f"Status: {status}")

def rename_with(filepath, new_name):
    os.rename(filepath, new_name)
    return new_name
  
def rename_with_underscore(filepath):
    file = filepath.split("/")[-1]
    new_filename = filepath.replace(" ", "_")
    # Check if the filename or path has changed (avoid unnecessary rename)
    if " " in file:
        os.rename(filepath, new_filename)
        return new_filename
    else:
        print(f"File {filepath} already has no spaces in path.")
        return filepath

def transcribe():
    global status, extension, filename, origname, project_dir, selected_model
    print(extension)
    print(filename)
    print(status)
    if status:
        if extension in ["m4a", "mkv"]:
            update_status("Converting to wav...")
            if extension == "m4a":
                print("converting m4a to wav")
                if converter.m4a_to_wav(filename, project_dir+"/temp.wav") == False: print("Error in convertion to wav")
            elif extension == "mkv":
                print("converting mkv to wav")
                if converter.mkv_to_wav(filename, project_dir+"/temp.wav") == False: print("Error in convertion to wav")
            else:
                print("Error in convertion to wav")
            now_path = project_dir+"/temp.wav"
            update_status("Converted to wav")
        else:
            filename
            shutil.copy(filename, project_dir+"/temp.wav")
        update_status("Transcripting")
        selected_model_str = selected_model.get()
        if selected_model_str == "": selected_model_str = "tiny"
        if whisper.transcribe(selected_model) == True:
            update_status("Transcripted")
            end_dest = filename.split(".")[0]+".txt"
            print(end_dest)
            shutil.copy("temp.txt", end_dest)
            update_status("Transcripted and saved")
        else:
            update_status("Error in transcripting")
    # rename_with(filename, origname)


root = tk.Tk()
root.title("Speech recogn1ser 3000")
root.geometry("400x300+50+100")  # 400x300 window, positioned 50 pixels from left and 100 pixels from top

selected_model = tk.StringVar()

label1 = tk.Label(root, text="Hello, You can tweak some parameters,\nselect a file and click recognise to recognise speech.")
label1.pack()
button1 = tk.Button(root, text="Select File", command=select_file)
button1.pack()
label2 = tk.Label(root, text="Selected File:")  # Label to display filename
label2.pack()
status_label = tk.Label(root, text="Status: No file selected")  # Label to display status
status_label.pack()
label3 = tk.Label(root, text="Select a model: ")  # Label to display status
label3.pack()
dropdown = tk.OptionMenu(root, selected_model, *available_models)
dropdown.pack()

button1 = tk.Button(root, text="Transcribe", command=transcribe)
button1.pack()

root.mainloop()
