# import library
import os
import random
import cv2
import pandas as pd
import numpy as np

#--------------------------
#configuration
#-------------------------- 

# from https://www.kaggle.com/code/hinepo/transfer-learning-with-timm-models-and-pytorch
class PROJECT_CFG:
    DATAP = './datap/'
    
    ### split train and validation sets
    split_fraction = 0.2
    random_seed = 42

#use this to get config
CFG=PROJECT_CFG()
