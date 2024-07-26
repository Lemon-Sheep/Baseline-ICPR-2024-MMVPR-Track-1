## This is the baseline model for the challenge on track 1: Multi-modal Tracking

This track aims to address the technical challenges associated with tracking objects in multi-modal data. The dataset for this task includes 500 multi-modal videos, with 400 allocated for training and the remaining 100 for testing. The main challenges include effectively fusing RGB, Depth, and Infrared modalities, managing different data qualities across modalities, and ensuring precise object tracking under various conditions. We look forward to innovative solutions that enhance tracking accuracy and robustness. Additionally, we anticipate advancements that push the boundaries of current multi-modal tracking technologies to tackle increasingly complex real-world scenarios.
![dyn-t1](https://github.com/user-attachments/assets/857eab82-b190-4591-b558-517f00c72a1c)

## :bookmark_tabs:Installation
* Install the conda environment
```
****
```
* Install the required packages:
```
pip install **
```
* Prepare the model
```
Download the model [here](), and put the model in the dir "root/pretrained/OSTrack_ep0300.pth.tar" and "root/pretrained/RDTTrack_ep0025.pth.tar".
```
* Prepare Datasets
```
Download the datasets we proved (you can get through the website), and then unzip them to your_dataset_dir.
```

## :car:Run
For example，if you want to run method on our dataset, you need to modify the ***** to
```
****
```
Then, run the train_rdtt.sh file. And you will get a final result file, which will use to evaluate on the website.

## :car:Evaluation
If you want to test methods on our method, run the test_rgbdt.sh file. 

## :Tips
The final document submit to the website should be organized strictly according to the baseline file's structure which you can download from the website.

=>for example, the  **result.zip**  is waht you need to submit：

<p>result.zip</p>
<p>&nbsp&nbsp|--baseline</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp|--001</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp|--002</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp...</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp|--100</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>
## :hearts: Acknowledgment
This project is based on [VIPT]().
Thanks for the excellent work.

