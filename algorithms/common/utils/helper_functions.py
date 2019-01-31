# -*- coding: utf-8 -*-
"""Common util functions for all algorithms.

- Author: Curt Park
- Contact: curt.park@medipixel.io
"""

import pickle

import numpy as np
import torch.nn as nn


def soft_update(local: nn.Module, target: nn.Module, tau: float):
    """Soft-update: target = tau*local + (1-tau)*target."""
    for t_param, l_param in zip(target.parameters(), local.parameters()):
        t_param.data.copy_(tau * l_param.data + (1.0 - tau) * t_param.data)


def fetch_desired_states_from_demo(demo_path: str) -> np.ndarray:
    """Return desired goal states from demonstration data."""
    with open(demo_path, "rb") as f:
        demo = pickle.load(f)

    demo = np.array(demo)
    goal_indices = np.where(demo[:, 4])[0]
    goal_states = demo[goal_indices][:, 0]

    return goal_states, goal_indices