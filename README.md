# PCB Fault Detection

**Website Link** - https://pcb-fault-detection.onrender.com

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
7. Deploying

Let us go through them one-by-one
## 1. Data Ingestion

### Data Ingestion
Data ingestion is the process of importing large, assorted data files from multiple sources into a single, cloud-based storage medium—a data warehouse, data mart or database—where it can be accessed and analyzed. As data may be in multiple different forms and come from hundreds of sources, it is sanitized and transformed into a uniform format using an extract/transform/load (ETL) process.

Data has been imported from : https://github.com/g0urav-hustler/External-Data/blob/main/PCBData.zip



## 2. Data Processing

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
    │   ├───images
    │   └───labels
    ├───group12000
    │   ├───images
    │   └───labels
    ├───group12100
    │   ├───images
    │   └───labels
    ├───group12300
    │   ├───images
    │   └───labels
    ├───group13000
    │   ├───images
    │   └───labels
    ├───group20085
    │   ├───images
    │   └───labels
    ├───group44000
    │   ├───images
    │   └───labels
    ├───group50600
    │   ├───images
    │   └───labels
    ├───group77000
    │   ├───images
    │   └───labels
    ├───group90100
    │   ├───images
    │   └───labels
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
For the base model we YOLO V8 Large model.
Reference - 
Notebook - []

