from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import json
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory


class WeatherRoot(BoxLayout):
    def show_current_weather(self, location):
        self.clear_widgets()
        current_weather = Factory.CurrentWeather()
        current_weather.location = location
        self.add_widget(current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        self.add_widget(AddLocationForm())

class LocationButton(ListItemButton):
    pass

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_ll(self):
        search_template = "http://api.openweathermap.org/data/2.5/weather?lat={}" \
                          "&lon={}&appid=d5366aed50c011a271178f9e85175646"
        ll = self.search_input.text.split(',')
        search_url = search_template.format(ll[0], ll[1])
        request = UrlRequest(search_url, self.found_location_ll)

    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/find?q={" \
                          "}&type=like&appid=d5366aed50c011a271178f9e85175646"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)


    def found_location(self, request, data):
        # print json.loads(data.decode())
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in data['list']]
        # self.search_results.item_strings = cities
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        # self.search_reaults._trigger_reset_populate()

    def found_location_ll(self, request, data):

        if data['cod'] == '404':
            cities = ["please enter right latitude and longitude"]
        else:
            cities = ["{} ({})".format(data['name'], data['sys']['country'])]
        # self.search_results.item_strings = cities
        self.search_results.adapter.data.extend(cities)

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()