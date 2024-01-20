"""
// Copyright (c) 2024 Robert Bosch GmbH
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published
// by the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import gpflow
import numpy as np
import tensorflow as tf
from typing import Optional, Dict

from .base_multioutput_flattened_kernel import BaseMultioutputFlattenedKernel

class BaseTransferKernel(BaseMultioutputFlattenedKernel):
    def get_source_parameters_trainable(self) -> bool:
        raise NotImplementedError
    def set_source_parameters_trainable(self, source_trainable: bool):
        raise NotImplementedError
    def get_target_parameters_trainable(self) -> bool:
        raise NotImplementedError
    def set_target_parameters_trainable(self, target_trainable: bool):
        raise NotImplementedError