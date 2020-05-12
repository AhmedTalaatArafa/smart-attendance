# You may need to restart your runtime prior to this, to let your installation take effect
# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
 
# import some common libraries
import numpy as np
import cv2
import random
 
# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog


File = open("Data2.txt","r+")

Path = File.readline()
File.truncate(0)
Path = Path.rstrip("\n")
im =cv2.imread(Path)
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7  # set threshold for this model
cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml")
predictor = DefaultPredictor(cfg)
outputs = predictor(im)
v = Visualizer(im[:,:,::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

with open("Data2.txt", "w") as txt_file:
        txt_file.write(str((len(outputs['instances'].pred_keypoints))))

File.close()
#print(len(outputs['instances'].pred_keypoints))
#D:\Study\5th year\Second Term\Image Processing\Project\build-untitled2-Desktop_Qt_5_13_2_MinGW_64_bit-Debug\collegestudents.jpg