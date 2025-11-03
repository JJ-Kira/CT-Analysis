"""
h5_utils.py
----------------
A simple utility module for saving and loading NumPy arrays
to and from HDF5 ('.h5') checkpoint files.

This module provides two functions:
- `save_array`: Save a single NumPy array to a dataset in an HDF5 file.
- `load_array`: Load a specific NumPy array from a dataset in an HDF5 file.

Example
-------
>>> import numpy as np
>>> from h5_checkpoint import save_array, load_array
>>> data = np.arange(10)
>>> save_array("checkpoint.h5", "my_array", data)
>>> loaded = load_array("checkpoint.h5", "my_array")
>>> np.array_equal(data, loaded)
True

Author: Julia Szczuczko
Date: 2025-11-01
"""

import numpy as np
import h5py
from typing import Any


def save_array(filepath: str, dataset_name: str, array: np.ndarray) -> None:
    """
Save a single NumPy array to an HDF5 file under the specified dataset name.

If the file or dataset already exists, it will be overwritten.

Parameters
----------
filepath : str
Path to the HDF5 file to save the array into.
dataset_name : str
Name of the dataset within the file (key) to store the array.
array : np.ndarray
The NumPy array to save.

Raises
------
OSError
If there is an error writing to the file.
    """
    with h5py.File(filepath, "a") as f:
        if dataset_name in f:
            del f[dataset_name]  # Overwrite existing dataset
        f.create_dataset(dataset_name, data=array)


def load_array(filepath: str, dataset_name: str) -> np.ndarray:
    """
Load a NumPy array from a specified dataset in an HDF5 file.

Parameters
----------
filepath : str
Path to the HDF5 file to read from.
dataset_name : str
Name of the dataset to load.

Returns
-------
np.ndarray
The loaded NumPy array.

Raises
------
KeyError
If the dataset does not exist in the file.
OSError
If the file cannot be opened.
    """
    with h5py.File(filepath, "r") as f:
        if dataset_name not in f:
            raise KeyError(f"Dataset '{dataset_name}' not found in '{filepath}'.")
        return f[dataset_name][()]


if __name__ == "__main__":
    # Simple usage example when run as a script
    arr = np.random.rand(3, 3)
    save_array("example_checkpoint.h5", "weights", arr)
    print("Saved array to 'example_checkpoint.h5'.")

    loaded_arr = load_array("example_checkpoint.h5", "weights")
    print("Loaded array:\n", loaded_arr)
