# -*- coding: utf-8 -*-


class LogStatus(object):
    DEFAULT = 0
    MESSAGE = 1
    CREATE = 2
    UPDATE = 3
    DELETE = 4

LOG_STATUS_CHOICES = (
    (LogStatus.DEFAULT, 'Default'),
    (LogStatus.MESSAGE, 'Message'),
    (LogStatus.CREATE, 'Create'),
    (LogStatus.UPDATE, 'Update'),
    (LogStatus.DELETE, 'Delete')
)
