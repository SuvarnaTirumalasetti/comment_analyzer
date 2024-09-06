import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# Function to execute the backend script
def run_backend(video_id):
    try:
        # Command to run your_script_name.py with the provided video_id as argument
        cmd = [sys.executable, "youcomment.py", "--videoid", video_id]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Assuming your_script_name.py prints results to stdout
        return result.stdout

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e.stderr}")
        return None

# Function to handle button click event
def analyze_comments():
    video_id = video_id_entry.get().strip()

    if not video_id:
        messagebox.showwarning("Warning", "Please enter a YouTube Video ID.")
        return

    try:
        # Call the backend function with the video_id
        backend_output = run_backend(video_id)

        if backend_output:
            # Display results in a messagebox or update a result label
            messagebox.showinfo("Analysis Results", backend_output)
            # Alternatively, update a label or text widget in your GUI
            # result_label.config(text=backend_output)
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("YouTube Comment Analyzer")
root.geometry("400x200")  # Set initial window size

# Styling and Layout
button_font = ("Arial", 12)
label_font = ("Arial", 12)

# Video ID Entry
video_id_label = tk.Label(root, text="Enter YouTube Video ID:", font=label_font)
video_id_label.pack(pady=10)
video_id_entry = tk.Entry(root, width=40)
video_id_entry.pack()

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Comments", command=analyze_comments, font=button_font)
analyze_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()