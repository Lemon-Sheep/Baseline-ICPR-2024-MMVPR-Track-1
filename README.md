## <img src="https://github.com/user-attachments/assets/4d9d5841-c29c-44bb-b63e-aca05927e114" alt="logo" width="100" /> Multi-Modal Visual Pattern Recognition Challenge-Track 1: Multi-Modal Tracking 


This is the official repository for the Multi-modal Visual Pattern Recognition-Track2 Multi-modal Tracking (ICPR 2024).
You can visit the challenge's official [website](https://prci-lab.github.io/mmvpr-workshop-icpr2024/) for more information, or you can directly participate in the competition on [codalab](https://codalab.lisn.upsaclay.fr/competitions/19861).

## :bookmark_tabs:Overview
This track aims to address the technical challenges associated with tracking objects in multi-modal data. The dataset for this task includes 500 multi-modal videos, with 400 allocated for training and the remaining 100 for testing. The main challenges include effectively fusing RGB, Depth, and Infrared modalities, managing different data qualities across modalities, and ensuring precise object tracking under various conditions. We look forward to innovative solutions that enhance tracking accuracy and robustness. Additionally, we anticipate advancements that push the boundaries of current multi-modal tracking technologies to tackle increasingly complex real-world scenarios.
![dyn-t1](https://github.com/user-attachments/assets/bf95735b-a16c-47ce-9f83-c55460f559ab)


## :bookmark_tabs:Installation
* Install the conda environment
```
conda create -n rdtt python=3.8
conda activate rdtt
```
* Install the required packages:
```
bash install_rdtt.sh
```
* Prepare the model
```
Dowmload the pretrained foundation model（OSTrack，RDTTrack） here: https://pan.baidu.com/s/1CnampD30EIwZ-jquEaj7pA (Extract code: 1234), and put it under ./pretrained/ such as "root/pretrained/OSTrack_ep0300.pth.tar" and "root/pretrained/RDTTrack_ep0025.pth.tar".
```
* Prepare Datasets
```
Download the datasets we proved (you can get through the website), and then unzip them to your_dataset_dir.
```

## :car:Train
You can train models with various modalities and variants by modifying train_rdtt.sh, And you will get a final result file, which will use to evaluate on the website.

## :car:Evaluation
If you want to test methods on our method, run the test_rgbdt.sh file. 

## :Tips
The final document submit to the website should be organized strictly according to the baseline file's structure which you can download from the website.

=>for example, the  **result.zip**  is waht you need to submit：

<p>--result.zip</p>
<p>&nbsp&nbsp|--baseline</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--001</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--002</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp...</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--100</p>
<p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp|--Prediction.txt</p>

## :hearts: Acknowledgment
This project is based on [VIPT](https://github.com/jiawen-zhu/ViPT ).
Thanks for the excellent work.

