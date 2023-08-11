from abc import ABC, abstractmethod

class ResultsLoader(ABC):
    @abstractmethod
    def load_results(self, src_file_path):
        pass
