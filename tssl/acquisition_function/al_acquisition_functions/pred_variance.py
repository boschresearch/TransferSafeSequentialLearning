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
from typing import Union, Sequence
import numpy as np
from tssl.acquisition_function.al_acquisition_functions.base_al_acquisition_function import BaseALAcquisitionFunction
from tssl.models.base_model import BaseModel


class PredVariance(BaseALAcquisitionFunction):
    def __init__(self, **kwargs):
        pass

    def acquisition_score(self, x_grid: np.ndarray, model: BaseModel, **kwargs):
        r"""
        x_grid: [N, D] array, location for which acquisiton score should be calcluated
        model: BaseModel, surrogate model used to calculate acquisition score

        return:
            [N, ] array, acquisition score (later maximize this to get query point)
        """
        _, pred_sigma = model.predictive_dist(x_grid)
        score = np.squeeze(pred_sigma) ** 2
        return score


if __name__ == "__main__":
    pass
