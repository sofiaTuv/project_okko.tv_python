import allure
from pages.main import MainPage
from pages.movie import MoviePage
from pages.search_result import SearchResultPage


@allure.tag('web')
@allure.label('layer', 'API')
@allure.label('owner', 's.tuvykina')
@allure.story('Поиск фильма')
@allure.link('https://okko.tv/', name='Testing')
class TestFilmSearch:
    main_p = MainPage()
    search_result_p = SearchResultPage()
    movie_p = MoviePage()

    @allure.title('Поиск фильма "Аферистка"')
    def test_search_by_full_name(self):
        self.search_test('Аферистка', 'Аферистка')

    @allure.title('Поиск фильма "Ирония судьбы, или с легким паром!"')
    def test_search_by_part_of_name(self):
        self.search_test('с легким паром', 'Ирония судьбы, или с легким паром!')

    @allure.title('Поиск фильма "Дивергент"')
    def test_search_by_foreign_name(self):
        self.search_test('divergent', 'Дивергент')

    @allure.title('Поиск фильма "Остаться в живых"')
    def test_search_by_foreign_keyboard_layout(self):
        self.search_test('jcnfnmcz d ;bds[ ', 'Остаться в живых')

    def search_test(self, search_text, film_name):
        # ACT
        self.main_p.search_for(search_text)
        self.search_result_p.select(film_name)
        # ASSERT
        self.movie_p.is_visible(film_name)
