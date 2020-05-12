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
#### Methodology
* Pre-processing
The pre-processing is a series of operations performed of scanned input image. It essentially enhances the image rendering for suitable segmentation.<br/>
* Paragraph Segmentation
<img src="https://user-images.githubusercontent.com/20180559/67069088-8ed31800-f199-11e9-9ff1-ce93c7a59143.jpg"><br/>
* Line Segmentation
<img src="https://user-images.githubusercontent.com/20180559/67069187-eec9be80-f199-11e9-8338-f6254e27afda.jpg"><br/>
* Handwriting Recognition
<img src="https://user-images.githubusercontent.com/20180559/67069304-449e6680-f19a-11e9-9846-c25ba51c2a7c.jpg"><br/>


#### 2.
