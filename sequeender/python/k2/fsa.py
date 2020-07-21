# Copyright (c)  2020  Xiaomi Corporation (author: Haowen Qiu)

# See ../../../LICENSE for clarification regarding multiple authors

import torch
from _k2 import DLPackFsa
from torch.utils.dlpack import to_dlpack


class Fsa(DLPackFsa):

    # TODO(haowen): add methods to construct object with Array2Size
    def __init__(self, indexes: torch.Tensor, data: torch.Tensor):
        super().__init__(to_dlpack(indexes), to_dlpack(data))
