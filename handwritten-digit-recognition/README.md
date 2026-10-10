# Handwritten Digit Recognition using CNN

A Python application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. It includes a Tkinter GUI where users can draw a digit and receive a prediction with a score.

## Features

- Trains a CNN on the MNIST handwritten-digit dataset.
- Normalizes image pixels and adds the grayscale channel dimension.
- Saves the trained model as `model.keras`.
- Provides a drawing canvas using Tkinter.
- Displays the predicted digit and the highest softmax output as a percentage.

## Project structure

```text
handwritten-digit-recognition/
├── app.py
├── train.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
    └── README.md
```

`model.keras` is generated locally by `train.py` and is not included by default.

## Requirements

- Python 3.10 or 3.11 recommended
- TensorFlow
- NumPy
- Pillow
- Tkinter (usually included with Python; some Linux distributions package it separately)

## Setup and run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/handwritten-digit-recognition.git
cd handwritten-digit-recognition
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train.py
```

On the first run, Keras downloads the MNIST dataset. The script trains the CNN for five epochs, prints the measured test accuracy, and saves `model.keras` in the project directory.

### 5. Launch the drawing application

```bash
python app.py
```

Draw a digit in the black canvas, click **Predict**, and view the predicted digit and score. Click **Clear** to start again.

> Run `train.py` before `app.py`, because the application expects `model.keras` to exist in the project directory.

## CNN architecture

The model in `train.py` uses these layers:

1. `Conv2D(32, 3×3, ReLU)` — learns local image features.
2. `MaxPooling2D(2×2)` — reduces feature-map dimensions.
3. `Conv2D(64, 3×3, ReLU)` — learns more complex feature combinations.
4. `MaxPooling2D(2×2)` — further reduces spatial dimensions.
5. `Flatten` — converts feature maps into a vector.
6. `Dense(64, ReLU)` — learns combinations of extracted features.
7. `Dense(10, Softmax)` — outputs scores for digit classes 0–9.

The model is compiled with the Adam optimizer and sparse categorical cross-entropy loss.

## How prediction works

1. The user draws a white digit on a black canvas.
2. The drawing is resized to `28 × 28` pixels.
3. Pixel values are normalized from `0–255` to `0–1`.
4. The image is reshaped to `(1, 28, 28, 1)`, representing one grayscale image in a batch.
5. The CNN returns ten softmax outputs.
6. `argmax` selects the class with the highest output; `max` is displayed as a percentage.

**Note:** the displayed percentage is the highest softmax output. It is not a guarantee that the prediction is correct or a calibrated probability of correctness.

## Results

Run `train.py` and enter your actual printed test accuracy here. Avoid claiming an estimated accuracy as a measured result.

## Limitations

- Recognizes single digits, not complete words or multi-digit numbers.
- Performance depends on how closely the user's drawing resembles MNIST examples.
- The drawing is resized directly to `28 × 28`; centering and scaling the digit more carefully may improve robustness.
- The current training script uses the MNIST test split as validation data during training and then evaluates on the same split. For a more rigorous evaluation, reserve a separate validation set from the training data and keep the test set untouched until final evaluation.

## Future improvements

- Center and scale the drawn digit before inference.
- Display scores for all ten digit classes.
- Add a confusion matrix and per-class evaluation.
- Improve the interface and add example screenshots.
- Explore alphabet recognition or camera-based input.

## References

- [3Blue1Brown — Neural Networks](https://www.3blue1brown.com/?topic=neural-networks)
- [Convolutional neural network — Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [TensorFlow documentation](https://www.tensorflow.org/)

## License

No license has been selected. Add a `LICENSE` file if you want to specify how others may use, modify, and distribute this project.
