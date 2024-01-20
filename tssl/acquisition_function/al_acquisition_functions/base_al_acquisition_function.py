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
from abc import abstractmethod
import numpy as np
from tssl.models.base_model import BaseModel


class BaseALAcquisitionFunction:
    @abstractmethod
    def acquisition_score(self, x_grid: np.ndarray, model: BaseModel, **kwargs) -> np.ndarray:
        r"""
        x_grid: [N, D] array, location for which acquisiton score should be calcluated
        model: BaseModel, surrogate model used to calculate acquisition score

        return:
            [N, ] array, acquisition score (later maximize this to get query point)
        """
        raise NotImplementedError
