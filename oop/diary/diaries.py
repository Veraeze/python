from oop.diary.diary import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def sizeofdiaries(self):
        return len(self.__diaries)

    def find_diary(self, username):
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary
        raise RuntimeError("Diary with this username does not exist")

    def delete(self, username, password):
        for diary in self.__diaries:
            if (diary.get_username() == username) & (diary.get_password() == password):
               return self.__diaries.remove(diary)
        raise RuntimeError("Diary with this username and password does not exist")



