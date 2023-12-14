import allure
from pages.sport import SportCategoryPage
from pages.movie import MoviePage
from pages.nature import NatureCategoryPage
from pages.main import MainPage


@allure.tag('web')
@allure.label('owner', 's.tuvykina')
@allure.story('Выбор фильма по категориям')
@allure.link('https://okko.tv/', name='Testing')
class TestCategory:
    main_p = MainPage()
    nature_p = NatureCategoryPage()
    movie_p = MoviePage()
    sport_p = SportCategoryPage()

    @allure.title('Выбор категории "Природа"')
    def test_nature_category(self):
        self.main_p.select_category('Природа')
        self.nature_p.is_visible()
        self.nature_p.select_first_movie()
        self.movie_p.is_genre(['Природа', 'Документальное'])

    @allure.title('Выбор категории "Спорт"')
    def test_sport_category(self):
        self.main_p.select_category('Спорт')
        self.sport_p.select_subcategory('Фигурное катание')
        self.sport_p.is_visible('Фигурное катание')
