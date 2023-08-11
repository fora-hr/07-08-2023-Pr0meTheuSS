from datetime import datetime
import re
from typing_extensions import override
from ResultsLoaderABC import ResultsLoader
import json

class ResultsLoaderFromTXT(ResultsLoader):

    def __init__(self):
        pass

    def calc_results_time_elapsed(self, data: dict):
        return {
            int(key): {"Result": item.get("Finish") - item.get("Start")} for key, item in data.items()
        }

    def parse_results(self, data: str):
        parsed_data = {}
        pattern = re.compile(r'(\d+) (start|finish) (\d{2}:\d{2}:\d{2}),(\d+)')
        for line in data:
            if line == "":
                continue

            match = pattern.match(line)
            if not match:
                print(f"Данные с результатами в неверном формате: {line}")
                raise ValueError
            number = int(match.group(1))
            action = match.group(2)
            timestamp_str = match.group(3)
            dist = match.group(4)

            timestamp = datetime.strptime(timestamp_str, '%H:%M:%S')
            
            if number not in parsed_data:
                parsed_data[number] = {"Start": None, "Finish": None, "Dist": None}
            
            if action == "start":
                parsed_data[number]["Start"] = timestamp
            elif action == "finish":
                parsed_data[number]["Finish"] = timestamp
            parsed_data[number]["Dist"] = dist
        
        return self.calc_results_time_elapsed(parsed_data)


    @override
    def load_results(self, file_path) -> dict:
        try:
            with open(file_path, 'r') as file:
                data = file.readlines()            
            return self.parse_results(data)

        except FileNotFoundError as e:
            print(f"Файл '{file_path}' не найден.")
            raise e
        except ValueError as e:
            raise e
