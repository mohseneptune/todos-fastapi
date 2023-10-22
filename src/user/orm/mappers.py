from infrastructure import mapper_registery
from user.entities import User
from user.orm.user_table import user_table


def start_user_mapper() -> None:
    mapper_registery.map_imperatively(User, user_table)
