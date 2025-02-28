from . import BaseController

class Controller(BaseController):
    def __init__(self):
        self.filepath = ""
        self.clf = None

    def update(self, target_lataccel, current_lataccel, state, future_plan):
        X_k = np.asarray([target_lataccel, current_lataccel, state, future_plan])
        y_pred = X_k.flatten()
        y_pred = 0 # TODO: remove
        return y_pred
