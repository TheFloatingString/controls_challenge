from . import BaseController
import numpy as np
import json


# class Controller(BaseController):
#     def __init__(self):
#         pass

#     def update(self, target_lataccel, current_lataccel, state, future_plan):
#         error = target_lataccel - current_lataccel
#         with open("config.json", "r") as openfile:
#             data_dict = json.load(openfile)
#         print(data_dict)
#         return 0.1 * error


class Controller(BaseController):
    """
    A simple PID controller
    """

    def __init__(
        self,
    ):
        # self.p = 0.3
        # self.i = 0.05
        # self.d = -0.1
        self.error_integral = 0
        self.prev_error = 0

    def update(self, target_lataccel, current_lataccel, state, future_plan):
        with open("config.json", "r") as openfile:
            data_dict = json.load(openfile)
        error = target_lataccel - current_lataccel
        self.error_integral += error
        error_diff = error - self.prev_error
        self.prev_error = error

        return data_dict['p']*error + data_dict['i']*self.error_integral + data_dict['d']*error_diff
        
        # return self.p * error + self.i * self.error_integral + self.d * error_diff