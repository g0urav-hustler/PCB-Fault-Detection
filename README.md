
  

  

# PCB Fault Detection

  

  

  

**Website Link** - https://huggingface.co/spaces/g0urav-hustler/PCB-Fault-Detection

  

  

  

## Introduction

  

  

Printed circuit boards (PCBs) are the primary component of any electronic design. Because of this surge in the demand for PCBs in the market, manufacturers are required to produce PCBs in large quantities. Therefore, maintaining the quality of such large numbers of PCBs is challenging. The main objective is to develop a PCB defect detection model that reduces the false detection rate and increases the production rate.To tackle this, in this project we are going to identify defects in a PCB using YOLO. You only look once (YOLO) is a state-of-the-art, real-time object detection system that uses algorithm which applies a single neural network to the full image, and then divides the image into regions and predicts bounding boxes and probabilities for each region.

  

  

Phases of the Project:

  

  

  

## Project Phase

  

  

Phases of the Project:

  

  

1. Data Ingestion

  

  

2. Data Processing

  

  

3. Base model

  

  

4. Training Model

  

  

5. Evaluation

  

  

6. WebApp

  

  

7. Deployment

  

  

  

Let us go through them one-by-one

  

  

## 1. Data Ingestion

  

  

**[Notebook](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/research/data_ingestion.ipynb)**

  

  

### Data Ingestion

  

  

Data ingestion is the process of importing large, assorted data files from multiple sources into a single, cloud-based storage medium—a data warehouse, data mart or database—where it can be accessed and analyzed. As data may be in multiple different forms and come from hundreds of sources, it is sanitized and transformed into a uniform format using an extract/transform/load (ETL) process.

  

  

  

Data has been imported from : https://github.com/g0urav-hustler/External-Data/blob/main/PCBData.zip

  

  

  

## 2. Data Processing

  

  

**[Notebook](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/research/data_processing.ipynb)**

  

### About the Dataset

  

  

The collection comprises 1,500 picture pairs, each consisting of a template image devoid of defects and a tested image that has been aligned and annotated with the positions of the six most prevalent PCB defects: open, short, mouse bite, spur, pinhole, and spurious copper.

  

  

  

### About the image

  

  

The linear scan CCD used to capture each image in this collection has a resolution of about 48 pixels per millimeter. The defect-free template pictures are manually examined and cleaned from sampling photos. The original size of the template and the tested image is around 16k x 16k pixels. They are then divided into several 640 × 640 pixels sub-images using a cropping process, then aligned using template matching methods. However, the 1500 defective PCB images and their annotation files are going to be primary resources for training our Deep Learning Model.

  

  

  

### About the image annotation

  

  

For each flaw in the tested photos, we utilize an axis-aligned bounding box with a class ID. Each annotated image owns an annotation file with the same filename, e.g.00041000_test.jpg, 00041000_temp.jpg and 00041000.txt are the tested image, template image and the corresponding annotation file. Each defect on the tested image is annotated as the format: **x1, y1, x2, y2, type**, where *(x1,y1)* and *(x2,y2)* are the *top-left* and the *bottom-right* corner of the bounding box of the defect and *type* is an *integer ID* that follows the matches: 0-background (not used), 1-open, 2-short, 3-mouse-bite, 4-spur, 5-copper, 6-pin-hole.

  

  

  

## Preparing images for training

  

  

Current folder structure:

  

  

```

  

└───PCBData

  

├───group00041

  

│ ├───images

  

│ └───labels

  

├───group12000

  

│ ├───images

  

│ └───labels

  

├───group12100

  

│ ├───images

  

│ └───labels

  

├───group12300

  

│ ├───images

  

│ └───labels

  

├───group13000

  

│ ├───images

  

│ └───labels

  

├───group20085

  

│ ├───images

  

│ └───labels

  

├───group44000

  

│ ├───images

  

│ └───labels

  

├───group50600

  

│ ├───images

  

│ └───labels

  

├───group77000

  

│ ├───images

  

│ └───labels

  

├───group90100

  

│ ├───images

  

│ └───labels

  

└───group92000

  

├───images

  

└───labels

  

```

  

  

The desired folder structure which is an entire repository of all the training images and validation-cross-validation images:

  

  

```

  

└─Processed_Data

  

└─raw_data

  

├─images

  

└─labels

  

└─processed_data

  

├─images

  

└─labels

  

└─split_data

  

├─train_data

  

└─val_data

```

  
  

## 3. Base model

  

[Notebook](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/research/prepare_base_model.ipynb)

  

For the base model we YOLO V8 Large model.

  

  

Reference - https://docs.ultralytics.com/models/yolov8/#key-features

  

  
  
  

  

## 4. Training Model

  

[Notebook](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/research/train_model.ipynb)

  

  

### Training Results

  

  

![Results image](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/results.png)

  

  

**Reference** - https://docs.ultralytics.com/modes/train/

  

  

## 5. Evaluation

  

[Notebook](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/research/model_evaluation.ipynb)

  

  

![F1-Curve Image](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/F1_curve.png)

  

**Reference** - https://docs.ultralytics.com/modes/val/

  
  

### Results

  

Here we show some results of our YOLO V8 Model. Our model achieves **_73.3% mAp, 92.0% F-score by traning model for 10 Epochs**.

  

Result pair 1:

<div  align=center><img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test1.jpg"  width="375"  style="margin:20">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test1_result.jpg"  width="375"  style="margin:20">

</div>

Result pair 2:

<div  align=center><img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test2.jpg"  width="375"  style="margin:20">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test2_result.jpg"  width="375"  style="margin:20">

</div>

Result pair 3:

<div  align=center><img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test3.jpg"  width="375"  style="margin:20">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<img  src="https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/test3_result.jpg"  width="375"  style="margin:20">

</div>

  

## 6. WebApp

  

**[Code](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/webapp/app.py)**

  

The webpage is build using Streamlit library . See [Reference](https://streamlit.io/)

  

**WEBAPP**

  
  

![Web Image](https://github.com/g0urav-hustler/PCB-Fault-Detection/blob/main/readme_sources/web_image.png)

## 7. Deployment

The Website is deployed on hugging face spaces using github action . 
[Reference](https://huggingface.co/docs/hub/spaces-sdks-streamlit)