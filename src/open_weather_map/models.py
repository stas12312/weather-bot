from pydantic import BaseModel


class Weather(BaseModel):
    """
    Модель статуса погоды
    """
    id: int  # Идентификатор погоды
    main: str  # Название погоды
    description: str  # Описание погоды
    icon: str  # Иконка погоды


class WeatherInfo(BaseModel):
    """
    Модель информации о погоде
    """
    dt: int  # Текущее время
    sunrise: int | None  # Время восхода
    sunset: int | None  # Время заката
    temp: float  # Температура
    feels_like: float  # Температура по ощущениям
    pressure: int  # Давление
    humidity: int  # Влажность
    dew_point: float  # Атмосферная температура
    uvi: float  # Ультрафиолетовый индекс
    clouds: int  # Облачность
    visibility: int  # Средняя видимость
    wind_speed: int  # Скорость ветра
    wind_deg: int  # Направление ветра
    weather: list[Weather]  # Статус погоды


class DailyTemp(BaseModel):
    """
    Температура на день
    """
    day: float
    night: float
    eve: float
    morn: float


class DailyFullTemp(DailyTemp):
    """
    Температура на день расширенная
    """
    min: float
    max: float


class DailyWeather(BaseModel):
    """
    Информация о погоде по дням
    """
    dt: int
    temp: DailyFullTemp
    feels_like: DailyTemp


class CommonWeather(BaseModel):
    """
    Модель общей информации
    """
    lat: float  # Широта
    lon: float  # Долгота
    timezone: str  # Временная зона
    timezone_offset: int  # Временной сдвиг относительно UTC


class OneCall(CommonWeather):
    """
    Модель для полной информации о погоде
    """
    current: WeatherInfo  # Текущая погод
    daily: list[DailyWeather]
