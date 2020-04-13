# Defines the actual configuration to be used to optimise

import torch
import numpy as np
from utils import MinMaxScaler

class Config():

    def __init__(self,scaler,input):
        self.input = input
        self.scaler = scaler

    #preforms preprocessing on the obtained features
    def get_scaled_paramaters(self):
        features = MinMaxScaler(self.scaler,self.input)
        return features
