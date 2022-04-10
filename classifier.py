class Classifier:

    def __init__(self, language: str):
        self.language = language

    def extract_intent(self, query: str):
        """Given a query, return the detected intent."""
        raise NotImplementedError
