from argparse import ArgumentParser

import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.utils.data import DataLoader, random_split

from torchvision.datasets.mnist import MNIST
from torchvision import transforms







def main():

    parser = ArgumentParser()
    parser.add_argument('--batch_size',default=32,type=int)

    transform = transforms.ToTensor()

    train_data = dataset.MNIST()
    test_data = dataset.MNIST()



if __name__ == '__main__':
    main()
