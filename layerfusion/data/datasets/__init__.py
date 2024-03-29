#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

from layerfusion.data.datasets.disk_dataset import DiskImageDataset

DATASET_SOURCE_MAP = {
    "disk": DiskImageDataset,
}
