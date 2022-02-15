from yoyo import read_migrations
from yoyo import get_backend


def migrate(
        user: str,
        password: str,
        host: str,
        db: str
) -> None:
    """
    Применение миграций
    :param user:
    :param password:
    :param host:
    :param db:
    :return:
    """
    dsn = f'postgres://{user}:{password}@{host}/{db}'

    backend = get_backend(dsn)
    migrations = read_migrations('/migrations')

    with backend.lock():
        # Apply any outstanding migrations
        backend.apply_migrations(backend.to_apply(migrations))
