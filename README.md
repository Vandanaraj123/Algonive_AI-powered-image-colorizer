AI-POWERED IMAGE COLORIZER

This project implements an AI-based Image Colorization system using a pre-trained deep learning model. The application converts grayscale (black & white) images into realistic colored images automatically.

The system leverages OpenCV’s Deep Neural Network (DNN) module and a Caffe-based pre-trained model to predict appropriate colors for each pixel in the image.

🎯 Objective

The objective of this project is to demonstrate the practical implementation of deep learning techniques in computer vision tasks, specifically automatic image colorization.

🛠 Technologies Used

Python

OpenCV (DNN Module)

NumPy

Caffe Pre-trained Model

📂 Project Structure
│── app.py                         # Main application file
│── Colorizer.py                   # Image colorization logic
│── Colorization_deploy_v2.prototxt  # Model architecture
│── pts_in_hull.npy                # Cluster center data
│── README.md                      # Project documentation


🚀 Installation & Execution
Step 1: Install Dependencies
pip install opencv-python numpy

Step 2: Download Model File

Download Colorization_release_v2.caffemodel and place it in the project directory.

Step 3: Run the Application
python app.py

📈 How It Works

The grayscale image is converted into the LAB color space.

The L channel (lightness) is passed into the deep neural network.

The model predicts the 'a' and 'b' color channels.

The channels are merged and converted back to RGB format to generate the final colorized image.

🔍 Applications

Restoration of old photographs

Historical image enhancement

Digital media processing

Computer vision research
