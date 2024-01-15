import allure

from pages.mood_reco import MoodRecommendationsPage
from pages.movie import MoviePage


@allure.tag('web')
@allure.label('layer', 'web')
@allure.label('owner', 's.tuvykina')
@allure.story('Выбор фильма с помощью рекомендаций')
@allure.link('https://okko.tv/', name='Testing')
class TestMainPage:
    mood_p = MoodRecommendationsPage()
    movie_p = MoviePage()

    @allure.title('Выбор фильма по подсказке "ужаснуться", "в компании"')
    def test_horror_company_recommendation(self):
        self.search_mood_film('ужаснуться','в компании', ['Ужасы', 'Триллеры'])

    @allure.title('Выбор фильма по подсказке "романтика", "вдвоем"')
    def test_romance_together_recommendation(self):
        self.search_mood_film('романтики', 'вдвоем', ['Мелодрамы', 'Драмы'])

    def search_mood_film(self, selected_mood: str, selected_company: str, genres: list[str]):
        # ACT
        self.mood_p.select_mood(selected_mood)
        self.mood_p.select_company(selected_company)
        self.mood_p.select_movie()
        # ASSERT
        self.movie_p.is_genre(genres)
