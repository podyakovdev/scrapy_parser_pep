from pep_parse.constants import ALLOWED_STATUSES


def check_status(status):
    if status in ALLOWED_STATUSES:
        return status
    raise Exception(f'Неизвестный статус! Добавьте {status} в ALLOWED_STATUS')
