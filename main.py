# Author: Dheeraj N Kashyap

import customtkinter as ctk
import tkinter
import os
import openai
from PIL import Image, ImageTk
import requests
import io

# Set your OpenAI API key here
openai.api_key = "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"

def generate():
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    user_prompt += " in style: " + style_dropdown.get()

    response = openai.Image.create(
        prompt=user_prompt,
        n=int(number_slider.get()),
        size="512x512"
    )

    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    print(image_urls)

    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        label.config(image=images[index])
        label.image = images[index]
        index = (index + 1) % len(images)
        label.after(3000, update_image, index)

    update_image()

root = ctk.CTk()
root.title("AI Image Generator")

ctk.set_appearance_mode("dark")

# Create two frames to divide the window
input_frame = ctk.CTkFrame(root)
input_frame.pack(side="top", expand=True, padx=20, pady=20, fill='both')

output_frame = ctk.CTkFrame(root)
output_frame.pack(side="top", expand=True, padx=20, pady=20, fill='both')

prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, padx=10, pady=10)
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row=0, column=1, padx=10, pady=10)

style_label = ctk.CTkLabel(input_frame, text="Style")
style_label.grid(row=1, column=0, padx=10, pady=10)
style_dropdown = ctk.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

number_label = ctk.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0)
number_slider = ctk.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9)
number_slider.grid(row=2, column=1)

generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

# Create a Label widget to display the generated image
label = tkinter.Label(output_frame)
label.pack()

root.mainloop()
