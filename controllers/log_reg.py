from . import BaseController
import numpy as np
import pickle

class Controller(BaseController):
    def __init__(self):
        self.pkl_filepath = ""
        self.clf = None

    def update(self, target_lataccel, current_lataccel, state, future_plan):
        X_k = np.asarray([target_lataccel, current_lataccel, state, future_plan])
        X_k = X_k.flatten()
        y_pred = self.clf.predict(X_k)
        y_pred = 0 # TODO: remove
        return y_pred
