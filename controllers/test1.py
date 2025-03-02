from . import BaseController
import numpy as np

class Controller(BaseController):
    def __init__(self):
        pass

    def update(self, target_lataccel, current_lataccel, state, future_plan):
        error = (target_lataccel - current_lataccel)
        return 0.1*error
