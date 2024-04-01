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
from scipy import stats
from tssl.enums.data_structure_enums import OutputType
from tssl.pools.base_pool import BasePool

class MultitaskPoolFromPools(BasePool):
    """
    This pool take multiple pools.
    It won't modify the data in each pool, but whenever data are retrieve or processed,
        it will decorate them in the flattened multi_output way (i.e. X: [N, D+1] array, with the last column being output indices)
    """
    def __init__(
        self,
        pool_list: Sequence[BasePool],
    ):
        super().__init__()
        self.output_type = OutputType.MULTI_OUTPUT_FLATTENED

        self.set_pool_list(pool_list)
        self.set_task_mode(self.output_dimension - 1) # default to the last pool

    def set_pool_list(self, pool_list: Sequence[BasePool]):
        self.pool_list = pool_list
        assert all([pool.output_type == OutputType.SINGLE_OUTPUT for pool in self.pool_list])

    def set_query_non_exist(self, query_non_exist_points:bool):
        super().set_query_non_exist(query_non_exist_points)
        for pool in self.pool_list:
            pool.set_query_non_exist(query_non_exist_points)

    def set_task_mode(self, pool_index: int):
        assert pool_index < len(self.pool_list)
        assert pool_index >= 0
        self.task_mode = pool_index

    @property
    def output_dimension(self):
        return len(self.pool_list)

    @property
    def task_index(self):
        return int(self.task_mode)

    def data_decorator(self, x, D:int, p:int):
        r"""
        x: [D,] array, [N, D] array or float (treat as [1, 1] array)
        return: [N, D+1] array, the last column is p
        """
        xx = np.atleast_2d(x)[..., :D]
        N = xx.shape[0]
        
        return np.hstack((xx, np.ones([N,1]) * p))
    
    def data_tuple_decorator(self, data, D:int, p:int):
        r"""
        data: (x, y) or (x, y, z)
            x: [D,] array, [N, D] array or float (treat as [1, 1] array)
            y: [1,], [N, 1], or float
            z: [Q,], [N, Q], or float, where Q is the number of safety controls
        
        decorate x into x': [N, D+1] array, the last column is p

        return: (x', y, z)
        """
        X = self.data_decorator(data[0], D, p)
        YZ_list = data[1:]
        return (X, *YZ_list)
    
    def _get_pool_d_p(self, task_index: int):
        pool = self.pool_list[task_index]
        d = pool.get_dimension()
        p = task_index
        return pool, d, p
    
    def get_max(self):
        pool, _, _ = self._get_pool_d_p(self.task_mode)
        if hasattr(pool, 'get_max'):
            return pool.get_max()
        else:
            raise NotImplementedError
    
    def get_constrained_max(
        self, 
        constraint_lower: float =-np.inf,
        constraint_upper: float = np.inf
    ):
        pool, _, _ = self._get_pool_d_p(self.task_mode)
        if hasattr(pool, 'get_constrained_max'):
            return pool.get_constrained_max(constraint_lower, constraint_upper)
        else:
            raise NotImplementedError

    def query(self, x, noisy: bool=True):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        return pool.query(x[...,:d], noisy=noisy)

    def batch_query(self, X, noisy: bool=True):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        return pool.batch_query(X[...,:d], noisy=noisy)

    def get_grid_data(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_grid_data(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)
    
    def get_data_from_idx(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_data_from_idx(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)
    
    def get_random_data(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_random_data(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)
    
    def get_random_data_in_box(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_random_data_in_box(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)

    def get_random_constrained_data(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_random_constrained_data(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)
    
    def get_random_constrained_data_in_box(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        # output_tuple may be (X, Y) or (X, Y, Z)
        output_tuple = pool.get_random_constrained_data_in_box(*args, **kwargs)
        return self.data_tuple_decorator(output_tuple, d, p)

    def get_dimension(self, *args, **kwargs):
        _, d, _ = self._get_pool_d_p(self.task_mode)
        return d

    def get_variable_dimension(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        return pool.get_variable_dimension(*args, **kwargs)

    def set_replacement(self,with_replacement: bool):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        pool.set_replacement(with_replacement=with_replacement)

    def get_context_status(self, *args, **kwargs):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        if hasattr(pool, 'get_context_status'):
            return pool.get_context_status(*args, **kwargs)
        else:
            raise NotImplementedError

    @property
    def __x(self):
        pool, d, p = self._get_pool_d_p(self.task_mode)
        return self.data_decorator(pool.possible_queries(), d, p)

    def possible_queries(self):
        return self.__x
            

