import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf

root = tk.Tk()  # main window
root.title("digit recognition")
root.geometry("400x450")

model = tf.keras.models.load_model("model.keras")  # load trained model

canvas_size = 280
canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="black")
canvas.pack(pady=20)
image = Image.new("L", (canvas_size, canvas_size), 0)
draw = ImageDraw.Draw(image)


def paint(event):
    brush_size = 12
    x1, y1 = event.x - brush_size, event.y - brush_size
    x2, y2 = event.x + brush_size, event.y + brush_size

    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
    draw.ellipse([x1, y1, x2, y2], fill=255)


def clear_canvas():
    canvas.delete("all")
    draw.rectangle((0, 0, canvas_size, canvas_size), fill=0)
    result_label.config(text="Draw a digit (0-9)")


def predict_digit():
    resized_img = image.resize((28, 28), Image.Resampling.LANCZOS)
    img_array = (np.array(resized_img) / 255.0).reshape(1, 28, 28, 1)
    predictions = model.predict(img_array, verbose=0)
    result_label.config(
        text=f"Prediction: {np.argmax(predictions)} "
             f"(score: {np.max(predictions) * 100:.1f}%)"
    )


canvas.bind("<B1-Motion>", paint)
btn_frame = tk.Frame(root)
btn_frame.pack()
tk.Button(btn_frame, text="Predict", font=("Arial", 12),
          command=predict_digit).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", font=("Arial", 12),
          command=clear_canvas).grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="Draw a digit", font=("Arial", 18))
result_label.pack(pady=20)

root.mainloop()
