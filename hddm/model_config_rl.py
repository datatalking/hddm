import numpy as np

model_config = {
    "ddm": {
    "params": ["v", "a", "z", "t", "alpha"],
    "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, 0.01], [3.0, 2.5, 0.9, 2.0, 0.99]],
    "n_params": 5,
    "default_params": [0.0, 1.0, 0.5, 1e-3, 0.5],
    "n_choices": 2,
    "choices": [-1, 1],
    },
    "angle": {
        "params": ["v", "a", "z", "t", "theta", "alpha"], ## v is actually scaler param
        "param_bounds": [[-3.0, 0.3, 0.2, 1e-3, -0.1, 0.01], [3.0, 2.0, 0.8, 2.0, 1.45, 0.99]],
        "n_params": 6,
        "default_params": [0.0, 1.0, 0.5, 1e-3, 0.0, 0.5],
        "n_choices": 2,
        "choices": [-1, 1],
    }
}