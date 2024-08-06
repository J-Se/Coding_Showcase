# cnn.py
#  Author: Eric Lykins
#
#  This file defines the CNN class used in the machine learning model.

import torch.nn as nn

class CNN(nn.Module):
    def __init__(self, side_length , num_channels=1, num_classes=4672):
        super(CNN, self).__init__()
        self.side_length = side_length
        self.features = nn.Sequential(
            nn.Conv2d(num_channels, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.classifier = nn.Sequential(
            nn.Linear(128 * self.side_length * self.side_length, 1024),
            nn.ReLU(),
            nn.Linear(1024, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(-1, 128 * self.side_length * self.side_length)
        return self.classifier(x)