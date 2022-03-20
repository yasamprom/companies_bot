from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class DataClass:
    def __init__(self):
        self.categories = ['IT', 'Коммуникации', 'Ювелирка']
        self.sub_categories = dict(
            {
                'IT': ['Google_disk', 'Photoshop', 'Adobe Premier', 'Google_maps'],
                'Коммуникации': ['Facebook', 'Instagram'],
                'Ювелирка': ['Тут какие-то описания, я не понял)']
            }
        )
        self.companies = dict({
            'Google_disk': 'Яндекс диск - disk.yandex.ru',
            'Adobe Premier': 'Мовави - movavi.com',
            'Facebook': 'Вк - vk.com',
            'Photoshop': 'ФОТОмастер - amssoft.ru',
            'Google_maps': 'Яндекс карты - maps.yandex.ru\n'
                           '2ГИС - 2gis.ru\n'
                           'Народная карта - n.maps.yandex.ru'

        })

    def categories_kb(self):
        cat_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        for key in self.categories:
            cat_kb.add(KeyboardButton(key))
        return cat_kb

    def back_to_menu(self):
        back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        back_kb.add(KeyboardButton('Меню'))
        return back_kb

    def get_list(self, company):
        return self.sub_categories[company]

    def companies_kb(self, category):
        cat_kb = ReplyKeyboardMarkup(resize_keyboard=True)
        for name in self.sub_categories[category]:
            cat_kb.add(KeyboardButton(name))
        cat_kb.add(KeyboardButton('Меню'))
        return cat_kb

    def compaines_text(self, company):
        return '✅ Вот аналоги, которые есть в нашей базе 👇\n' \
               + self.companies[company]
