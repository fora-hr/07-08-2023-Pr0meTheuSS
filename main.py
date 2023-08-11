import datetime
from CompetitorsLoaderFromJSON import JSONCompetitorsLoader
from TXTResultsLoader import ResultsLoaderFromTXT

competitors_file_path = "competitors2.json"
results_file_path = "results_RUN.txt"

table_headers = ["Занятое место", "Нагрудный номер", "Имя", "Фамилия", "Результат"]
table_format = "{:<3} {:<15} {:<20} {:<20} {:8}" 

# Функции для доступа к необходимым полям тупла с результатами забега
def get_number(res: tuple) -> int:
    return res[0]

def verify_time(time) -> bool:
    ...
    return time > datetime.timedelta(0)

def get_time(result: tuple) -> str:
    timedelta = result[1]["Result"]
    if verify_time(timedelta):
        return str(timedelta)
    raise ValueError("Невалидное время в результате забега: {}".format(str(timedelta)))


if __name__ == "__main__":
    '''
        В интерфейсах загрузчиков данных необходимости для решения задачи нет.
        Но при реализации компонента, обрабатывающего данные, такие интерфейсы упростили бы
        расширяемость модуля(при появлении новых форматов и задач) и внедрение зависимостей.
    '''
    competitors_loader = JSONCompetitorsLoader()
    results_loader = ResultsLoaderFromTXT()

    try:
        competitors = competitors_loader.load_competitors(competitors_file_path)
        results  = list(results_loader.load_results(results_file_path).items())
        sort = sorted(results, key=lambda x: x[1]["Result"])

        print(table_format.format(*table_headers))
        for idx, result in enumerate(sort):
            number = get_number(result)
            time = get_time(result)
            print(table_format.format(idx+1, number, competitors[number]["Name"], competitors[number]["Surname"], time))

    # Условиями задачи не установлен порядок обработки ошибок и исключений, поэтому просто прерываю работу программы (fail fast)
    # Ловлю всё
    except Exception as e:
        print("Приложение завершилось с исключением.")
        print(e)
        ...
        exit(1)

    print("Таблица успешно построена.")
