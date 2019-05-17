"""Just another implementation on LayoutGAN.
Use TensorFlow, TensorFlow-Graphics

Copyright ©2019-current, Junru Zhong, all rights reserved.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np


# Enable eager execution. Not necessary for TensorFlow 2.0+.
# tf.enable_eager_execution()

def load_mnist():
    """This function loads the MNIST dataset from TensorFlow official Datasets."""
    # Download from Google
    mnist_builder = tfds.builder('mnist')
    mnist_builder.download_and_prepare()
    # Transfer to TensorFlow `Dataset` object.
    mnist_train = mnist_builder.as_dataset(split=tfds.Split.TRAIN)
    print(mnist_train)
    # Transfer MNIST images to tensors with geometry information in the iterator.


if __name__ == '__main__':
    load_mnist()
