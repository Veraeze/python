import datetime


class Entry:
    def __init__(self, id_no, title, body):
        self.__id_no = id_no
        self.__title = title
        self.__body = body
        self.__dateCreated = datetime.datetime.now()

    def get_id_no(self):
        return self.__id_no

    def edit(self, title, body):
        self.__title = title
        self.__body = body

