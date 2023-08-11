from abc import ABC, abstractmethod

class CompetitorsLoader(ABC):
    @abstractmethod
    def load_competitors(self, src_file_path):
        pass
