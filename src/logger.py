import logging

app_logger = logging.getLogger('weather_bot')
app_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(logging.BASIC_FORMAT)

ch.setFormatter(formatter)
app_logger.addHandler(ch)
