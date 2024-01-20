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
import pandas as pd
import numpy as np

from tssl.data_sets.base_data_set import StandardDataSet
import os


class Engine1(StandardDataSet):
    def __init__(self, base_path="U:\\Projects\\experiments\\data\\engine"):
        super().__init__()
        self.file_path = os.path.join(base_path, 'engine1_normalized.xlsx')
        self.safety_path = os.path.join(base_path, 'safety_constraint.xlsx')
        self.constrain_input = True
        self.name = "Engine1"

    def load_data_set(self):
        data = pd.read_excel(self.file_path, sheet_name = 'data', header=[0, 1], index_col=[0])
        x_cols = ['engine_speed', 'engine_load', 'intake_valve_opening', 'air_fuel_ratio']
        y_cols = ['specific_fuel_consumption', 'temperature_exhaust_manifold', 'temperature_in_catalyst', 'engine_roughness_v', 'engine_roughness_s', 'HC', 'NOx']
        
        X_table = data[x_cols]
        Y_table = data[y_cols]

        if self.constrain_input:
            safety_df = pd.read_excel(self.safety_path, sheet_name = 'engine1_normalized', header=[0,1], index_col=0)
            mask = (X_table >= safety_df.loc['lower_bound', x_cols]) & (X_table <= safety_df.loc['upper_bound', x_cols])
            mask = mask.all(axis=1).to_numpy().reshape(-1)
            self.x = X_table[mask].to_numpy()
            self.y = Y_table[mask].to_numpy()
            self.data_index = data.index[mask].to_numpy()
        else:
            self.x = X_table.to_numpy()
            self.y = Y_table.to_numpy()
            self.data_index = data.index.to_numpy()
        self.input_names = x_cols
        self.output_names = y_cols
        self.length = self.x.shape[0]
        self.input_dimension = len(x_cols)
        self.output_dimension = len(y_cols)


class Engine2(StandardDataSet):
    def __init__(self, base_path="."):
        super().__init__()
        self.file_path = os.path.join(base_path, 'engine2_normalized.xlsx')
        self.safety_path = os.path.join(base_path, 'safety_constraint.xlsx')
        self.constrain_input = True
        self.name = "Engine2"

    def load_data_set(self):
        data = pd.read_excel(self.file_path, sheet_name = 'data', header=[0, 1], index_col=[0])
        x_cols = ['engine_speed', 'engine_load', 'intake_valve_opening', 'air_fuel_ratio']
        y_cols = ['specific_fuel_consumption', 'temperature_exhaust_manifold', 'temperature_in_catalyst', 'engine_roughness_v', 'engine_roughness_s', 'HC', 'NOx']
        
        X_table = data[x_cols]
        Y_table = data[y_cols]
        
        if self.constrain_input:
            safety_df = pd.read_excel(self.safety_path, sheet_name = 'engine1_normalized', header=[0,1], index_col=0)
            mask = (X_table >= safety_df.loc['lower_bound', x_cols]) & (X_table <= safety_df.loc['upper_bound', x_cols])
            mask = mask.all(axis=1).to_numpy().reshape(-1)
            self.x = X_table[mask].to_numpy()
            self.y = Y_table[mask].to_numpy()
            self.data_index = data.index[mask].to_numpy()
        else:
            self.x = X_table.to_numpy()
            self.y = Y_table.to_numpy()
            self.data_index = data.index.to_numpy()
        self.input_names = x_cols
        self.output_names = y_cols
        self.length = self.x.shape[0]
        self.input_dimension = len(x_cols)
        self.output_dimension = len(y_cols)


if __name__ == "__main__":
    data_loader = Engine1()
    data_loader.load_data_set()
    print(data_loader.length)
    print(data_loader.input_dimension)
    print(data_loader.output_dimension)
    
    data_loader = Engine2()
    data_loader.load_data_set()
    print(data_loader.length)
    print(data_loader.input_dimension)
    print(data_loader.output_dimension)
    