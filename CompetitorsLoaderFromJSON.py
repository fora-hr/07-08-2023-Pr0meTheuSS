from typing_extensions import override
from CompetitorsLoaderABC import CompetitorsLoader
import json

class JSONCompetitorsLoader(CompetitorsLoader):

    def __init__(self):
        pass

    @override
    def load_competitors(self, file_path) -> []:
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                return {int(key): value for key, value in json_data.items()}
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле '{file_path}'.")
        except ValueError:
            print(f"Ошибка формата данных '{file_path}'.")
