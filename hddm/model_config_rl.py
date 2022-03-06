from .simulators import boundary_functions as bf
import numpy as np

model_config = {
    "ddm": {
        "params": ["v", "a", "alpha", "t"], ## v is actually scaler param
        "param_bounds": [[0.1, 0.8, 0.5, 0.5], [3.0, 2.0, 1.0, 1.8]],
        "n_params": 4,
        "default_params": [1.0, 1.0, 0.8, 0.7],
        "n_choices": 2,
        "choices": [-1, 1],
    },
    "angle": {
        "params": ["v", "a", "z", "t", "theta", "alpha"], ## v is actually scaler param
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.2, 1e-3, -0.1], [3.0, 2.0, 0.8, 2.0, 1.45]],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, 0.0, 0.0],
            [2.5, 2.0, 0.9, 2.0, (np.pi / 2 - 0.2)],
        ],  # [(-2.5, 2.5), (0.2, 2.0), (0.1, 0.9), (0.0, 2.0), (0, (np.pi / 2 - .2))]
        "boundary": bf.angle,
        "n_params": 5,
        "default_params": [0.0, 1.0, 0.5, 1e-3, 0.0],
        "hddm_include": ["z", "theta"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "theta": 0.1, "theta_std": 0.2},
    }
}