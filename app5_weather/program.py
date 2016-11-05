import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')


def main():
    print_the_header()

    zipcode = input('What zipcode do you want the weather for (55432)? ')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(report.loc, report.temp, report.scale, report.cond))


def print_the_header():
    print('----------------------------------')
    print('           Weather App')
    print('----------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text


def get_weather_from_html(html):
    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    location = cleanup_text(location)
    location = find_city_and_state_from_location(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=location)
    return report


def cleanup_text(text: str):  # doing this allows pycharm to give help on 'text' variable suggesting string methods
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(location: str):
    parts = location.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()

