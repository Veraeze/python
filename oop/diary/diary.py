from oop.diary.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__size_of_entries = 0
        self.__entries = []

    def unlock_diary(self, password):
        self.validate(password)
        self.__is_locked = False

    def is_locked(self):
        return self.__is_locked

    def validate(self, password):
        if password != self.__password:
            raise RuntimeError("Incorrect password")
        return password == self.__password

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title, body):
        if self.__is_locked:
            raise RuntimeError("Diary is locked! Unlock to perform action")
        self.__size_of_entries += 1
        id_no = self.generate_id()
        entry = Entry(id_no, title, body)
        self.__entries.append(entry)

    def numberofentries(self):
        return len(self.__entries)

    def generate_id(self):
        return int(f'22{self.__size_of_entries}')

    def delete_entry(self, id_no):
        self.__entries.remove(self.find_entry(id_no))

    def find_entry(self, id_no):
        if self.__is_locked:
            raise RuntimeError("Diary is locked! Unlock to perform action")
        for entry in self.__entries:
            if entry.get_id_no() == id_no:
                return entry
        raise RuntimeError("Entry cannot be found")

    def update_entry(self, id_no, title, body):
        if self.__is_locked:
            raise RuntimeError("Diary is locked! Unlock to perform action")
        entry = self.find_entry(id_no)
        entry.edit(title, body)
        self.__entries[self.find_indexof(id_no)] = entry

    def find_indexof(self, id_no):
        for index, value in enumerate(self.__entries):
            if value.get_id_no() == id_no:
                return index
        raise RuntimeError("Entry cannot be found")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password









