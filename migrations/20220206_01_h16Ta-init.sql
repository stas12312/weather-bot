-- Init
-- depends:
-- Таблица для хранения пользователей Telegram
CREATE TABLE tg_user
(
    user_id    BIGINT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name  VARCHAR(255) DEFAULT '',
    username   VARCHAR(255) DEFAULT '',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);


-- Таблица для погодного виджета
CREATE TABLE user_weather_widget
(
    user_id         BIGINT,
    name            VARCHAR(255),
    timezone_offset INT,
    latitude        FLOAT,
    longitude       FLOAT,
    city_name       VARCHAR(255),
    settings        jsonb, -- В настройках хранится: Время уведомления, отображаемые данные
    is_default      BOOLEAN,

    FOREIGN KEY (user_id) REFERENCES tg_user (user_id)
);

CREATE INDEX user_weather_widget_id_idx ON user_weather_widget (user_id);

