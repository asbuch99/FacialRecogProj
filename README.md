# Facial Recognition Project

This project is aimed at developing a air gapped facial recognition system using Python and various libraries.  
More details can be found in the Project Report.

It involves the following tasks:

## Objectives:

1. Implementing a facial detection algorithm.
2. Training a model to recognize faces.
3. Integrating the trained model into a real-time application.
4. Deploying the application to various platforms.

## Project Structure:

The project is organized as follows:

- **src/**: Contains the source code for the facial recognition system.
  - `facial_detection.py`: Script for detecting faces in images or video streams.
  - `facial_recognition.py`: Script for training and recognizing faces.
  - `app.py`: Main application script for real-time face recognition.
- **data/**: Contains datasets for training the facial recognition model.
  - `faces/`: Directory containing labeled face images for training.
- **models/**: Saved models after training.
- **docs/**: Documentation files.
- **requirements.txt**: Dependencies required to run the project.

## Usage:

1. Clone the repository:
    ```
    git clone https://github.com/asbuch99/FacialRecogProj.git
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Train the model:
    ```
    python src/facial_recognition.py --train
    ```

4. Run the real-time face recognition application:
    ```
    python src/app.py
    ```

## Contributions:

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.
