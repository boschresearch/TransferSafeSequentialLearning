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
from enum import Enum, IntEnum
import numpy as np


class PriorSettings(IntEnum):
    STANDARD = 1
    HIGH_NOISE = 2
    FLEXIBLE_ZERO_ONE = 3


PRIOR_SETTING = PriorSettings.STANDARD

if PRIOR_SETTING == PriorSettings.STANDARD:

    EXPECTED_OBSERVATION_NOISE = 0.1
    NOISE_VARIANCE_EXPONENTIAL_LAMBDA = 1.0 / np.power(EXPECTED_OBSERVATION_NOISE, 2.0)
    KERNEL_VARIANCE_GAMMA = (2.0, 3.0)
    KERNEL_LENGTHSCALE_GAMMA = (2.0, 2.0)
