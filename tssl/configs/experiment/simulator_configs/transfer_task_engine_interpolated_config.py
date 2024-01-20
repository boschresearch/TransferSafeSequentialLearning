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
from typing import List, Union, Sequence
from tssl.configs.experiment.simulator_configs.base_simulator_config import BaseSimulatorConfig
from tssl.enums.simulator_enums import InitialDataGenerationMethod


class TransferTaskEngineInterpolatedBaseConfig(BaseSimulatorConfig):
    n_pool: int
    data_path: str
    additional_safety: bool = True
    data_set: str = 'engine_oracle'

    initial_data_source: InitialDataGenerationMethod = InitialDataGenerationMethod.GENERATE
    target_box_a = [-0.5, 0.5, -2.5, -2.5]
    target_box_width = [1.0, 1.0, 5, 5]
    
    input_idx: Sequence[Union[int, bool]]=[0, 1, 2, 3]
    output_idx: Sequence[Union[int, bool]]=[0]
    safety_idx: Sequence[Union[int, bool]]=[1]
    seed: int=1234
    name: str='transfer_task_engine_interpolated'

class TransferTaskEngineInterpolated_be_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[0]
    name: str='transfer_task_engine_interpolated_be'

class TransferTaskEngineInterpolated_TEx_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[1]
    name: str='transfer_task_engine_interpolated_TEx'

class TransferTaskEngineInterpolated_PI0v_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[3]
    name: str='transfer_task_engine_interpolated_PI0v'

class TransferTaskEngineInterpolated_PI0s_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[4]
    name: str='transfer_task_engine_interpolated_PI0s'

class TransferTaskEngineInterpolated_HC_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[5]
    name: str='transfer_task_engine_interpolated_HC'

class TransferTaskEngineInterpolated_NOx_Config(TransferTaskEngineInterpolatedBaseConfig):
    output_idx: Sequence[Union[int, bool]]=[6]
    name: str='transfer_task_engine_interpolated_NOx'
