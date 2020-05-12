# Smart Attendance System 

# It is our contribution in **ASU-CVC** competition.
This project is an attendance system that transfer handwritten names into strings can be stored in Excel sheets or you can modify it to be recorded in Databas.
Also user can attach a photo for students to count the actual number of attendants.

## We have two models :
### 1. HandwrittenTextRecognition trained by [I AM Handwriting Dataset](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database)
We had a great challenge in this model as the results were not applicable to be used to search in a database or Excel sheet due to missing or changing any letter of the handwritten name or any wrong spaces.<br/>So we did the following :<br/>
We used a scoring function to make a unique score for every name predected from the model and we combared it with the scores from the Excel sheet to make the matching.<br/>
### 2. Detectron2
Detectron2 is Facebook AI Research's next generation software system that implements state-of-the-art object detection algorithms.

## Methodologies
### Line Segmentation
line segmentation is done through pre-processing, feature extraction and segmentation. Line Segmentation is used to identify the lines present in the paragraph. This is important as many people have a tendency to not write in a straight line.
<img src="https://camo.githubusercontent.com/7ccf78e2766e528a14189c31ea3894992c443ad4/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a6a4d6b4f3768792d3166305a464854335332694830512e706e67">
<img src="https://camo.githubusercontent.com/d61ffdb9d133e770b1bdb3375cd833348cc6cbbf/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313030302f312a4a4a47774c584a4c2d6256377a7366726677383465772e706e67">
### Handwriting Recognition
he final model is the handwriting recognition model which takes a line as input and converts the line into digital text. This model consits of a CNN-biLSTM architecture. The loss used is the CTC (Connectionist Temporal Classification) loss.
<img src="https://user-images.githubusercontent.com/20180559/67068512-ea040b00-f197-11e9-8665-8afa5daf00f6.png">
Here is the CNN-biLSTM architecture model.

The input lines are sent into the CNN to extract features from similar patterns. These image features are then sent to a sequential learner which are the bidirectional LSTMs which are then sent to the output string that predict the character based on the alphabet with the highest predicted value given by the model.

### Why Detectron2
![image](https://user-images.githubusercontent.com/29764281/81747879-263ae800-94a9-11ea-9ac8-7d86bb0c7179.png)

We use detectron2 for checking the number of the students in the class to make sure there's no way to cheat. We achieve that through taking an photo or video stream of a camera(webcam or phone camera) and return number of person instances in this photo.

## Build & Install the entire project
### Build and Install Detectron2
#### Requirements
- Linux or macOS
- Python ≥ 3.6
- PyTorch ≥ 1.3
- [torchvision](https://github.com/pytorch/vision/) that matches the PyTorch installation.
	You can install them together at [pytorch.org](https://pytorch.org) to make sure of this.
- OpenCV, optional, needed by demo and visualization
- gcc & g++ ≥ 4.9
After having the above dependencies, run:
```
# install dependencies: (use cu101 because colab has CUDA 10.1)
pip install -U torch==1.5 torchvision==0.6 -f https://download.pytorch.org/whl/cu101/torch_stable.html 
pip install cython pyyaml==5.1
pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
pip install detectron2==0.1.2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/index.html
cd detectron2; python setup.py install
```
