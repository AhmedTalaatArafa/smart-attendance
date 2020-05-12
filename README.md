# Smart Attendance System 

# It is our contribution in **ASU-CVC** competition.
This project is an attendance system that transfer handwritten names into strings can be stored in Excel sheets or you can modify it to be recorded in Databas.
Also user can attach a photo for students to count the actual number of attendants.

## We have two models :
### 1.HandwrittenTextRecognition trained by [I AM Handwriting Dataset](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database)
We had a great challenge in this model as the results were not applicable to be used to search in a database or Excel sheet due to missing or changing any letter of the handwritten name or any wrong spaces.<br/>So we did the following :<br/>
We used a scoring function to make a unique score for every name predected from the model and we combared it with the scores from the Excel sheet to make the matching.<br/>
#### Dependency
* mxnet
* pandas
* matplotlib
* numpy
* skimage
## Methodology
### Line Segmentation
line segmentation is done through pre-processing, feature extraction and segmentation. Line Segmentation is used to identify the lines present in the paragraph. This is important as many people have a tendency to not write in a straight line.
<img src="https://camo.githubusercontent.com/7ccf78e2766e528a14189c31ea3894992c443ad4/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a6a4d6b4f3768792d3166305a464854335332694830512e706e67">
<img src="https://camo.githubusercontent.com/d61ffdb9d133e770b1bdb3375cd833348cc6cbbf/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313030302f312a4a4a47774c584a4c2d6256377a7366726677383465772e706e67">
* Handwriting Recognition
<img src="https://user-images.githubusercontent.com/20180559/67069304-449e6680-f19a-11e9-9846-c25ba51c2a7c.jpg"><br/>


#### 2.
