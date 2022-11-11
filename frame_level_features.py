# extract the CNN features corresponding to each frame 
# DNN implemented in Pytorch

from torchvision import models
import torch

class FrameFeatures:

    def __init__(self, frames_path, network = 'resnet50'):

        self.frames_path = frames_path
        self.network = network

        self.network_dict = {'resnet18':models.resnet18(pretrained = True),'resnet50': models.resnet50(pretrained = True)}
                                
        self.get_network()


    def get_network(self):

        model = self.network_dict[self.network]
        self.feature_extractor = torch.nn.Sequential(*list(model.children())[:-1])
    
    def get_features(self, x):
        # x should be of the size -> (bs, 3, 224, 224)
        return self.feature_extractor(x)

    
    def preprocessing(self):

        







    
    

    


