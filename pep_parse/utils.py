from pep_parse.constants import ALLOWED_STATUS


def check_status(status):
    if status in ALLOWED_STATUS:
        return status
    raise Exception(f'Неизвестный статус! Добавьте {status} в ALLOWED_STATUS')
