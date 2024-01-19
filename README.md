## Проект UI автотестов на онлайн-кинотеатр okko.tv
![This is an image](resources/images/okkotv.png)

<h3> Список реализованных проверок:</h3>

* Поиск фильма по поисковой строке 
* Выбор фильма по подсказке и проверка на соответствующий жанр 
* Выбор фильма по категории и проверка на соответствующий жанр
  
----
### Используется:
<p  align="center">
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="resources/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="resources/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>

----
### Локальный запуск

> Для локального запуска необходимо выполнить команду в СLI:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests/
```

> Получение Allure отчета
```bash
allure serve allure-results/
```

----
### <img width="5%" title="Jenkins" src="resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Jenkins](https://jenkins.autotests.cloud/job/python_project_okko.tv/)

#### При нажатии на "Build with Parameters" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide
![This is an image](resources/images/jenkins.png)

<!-- Allure report -->
----
### <img width="5%" title="Allure Report" src="resources/logo/allure_report.png"> Allure report
### [Report](https://jenkins.autotests.cloud/job/python_project_okko.tv/18/allure/)
#### Результаты тестов в Allure отчете
![This is an image](resources/images/results.png)

#### Список тест кейсов
![This is an image](resources/images/test.png)

#### Пример отчета о прохождении ui-теста
![This is an image](resources/images/test_example.png)

#### Видео прохождение теста
![This is an image](resources/images/successfull_test.gif)

#### Видео и отчет о прохождении теcта с багом на сайта
![This is an image](resources/images/mood_tests.png)
![This is an image](resources/images/failed_test.gif)

<!-- Allure TestOps -->
----
### <img width="5%" title="Allure TestOps" src="resources/logo/allure_testops.png"> Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/3977/dashboards)

#### Dashboard с результатами тестирования
![This is an image](resources/images/dash.png)

#### Список общих тестов
![This is an image](resources/images/tests_testops.png)

#### Пример отчета 
![This is an image](resources/images/nature.png)

#### История запуска тестовых наборов
![This is an image](resources/images/launches.png)

<!-- Jira -->
----
### <img width="5%" title="Jira" src="resources/logo/jira.png"> Jira

### [Jira](https://jira.autotests.cloud/browse/HOMEWORK-1061)

#### Настроенная через Allure TestOps интеграция с Jira

![This is an image](resources/images/jira_okko.png)


<!-- Telegram -->
----
### <img width="5%" title="Telegram" src="resources/logo/tg.png"> Telegram

#### Уведовление в Telegram bot после прохождения тестов

![This is an image](resources/images/tg_okkotv.png)


