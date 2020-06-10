from models.base_model import BaseModel


class NullModel(BaseModel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.labels = []

    def fit_partial(self, x, y=None):

        return self

    def score_partial(self, x):

        return 0.5
