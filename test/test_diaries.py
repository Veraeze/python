from unittest import TestCase
from oop.diary.diaries import Diaries


class Test(TestCase):
    def test_that_diaries_can_add_diary(self):
        diaries = Diaries()

        self.assertEqual(0, diaries.sizeofdiaries())

        diaries.add("cynthia", "password")
        self.assertEqual(1, diaries.sizeofdiaries())

    def test_that_diaries_can_add_more_than_one_diary(self):
        diaries = Diaries()

        self.assertEqual(0, diaries.sizeofdiaries())

        diaries.add("cynthia", "happy")
        diaries.add("hannah", "password")

        self.assertEqual(2, diaries.sizeofdiaries())

    def testThatDiariesCanFindDiaryByUsername(self):
        diaries = Diaries()

        diaries.add("cynthia", "password")
        diaries.add("esther", "password2")
        diaries.add("ann", "password2")

        self.assertEqual(3, diaries.sizeofdiaries())

        diary1 = diaries.find_diary("cynthia")
        self.assertEqual("cynthia", diary1.get_username())

        diary2 = diaries.find_diary("ann")
        self.assertEqual("ann", diary2.get_username())

        diary3 = diaries.find_diary("esther")
        self.assertEqual("esther", diary3.get_username())

    def testThatExceptionIsThrown_FindDiaryByUsernameThatDoesNotExist(self):
        diaries = Diaries()

        diaries.add("cynthia", "password")

        self.assertEqual(1, diaries.sizeofdiaries())

        with self.assertRaises(RuntimeError):
            diaries.find_diary("ann")

    def testThatDiariesCanDeleteDiary(self):
        diaries = Diaries()

        diaries.add("cynthia", "password")
        diaries.add("esther", "password2")
        diaries.add("ann", "password3")

        self.assertEqual(3, diaries.sizeofdiaries())

        diaries.delete("esther", "password2")
        self.assertEqual(2, diaries.sizeofdiaries())

    def testThatExceptionIsThrown_DeleteDiaryWithWrongUsernameOrPassword(self):
        diaries = Diaries()

        diaries.add("cynthia", "password")
        diaries.add("esther", "password2")

        self.assertEqual(2, diaries.sizeofdiaries())

        with self.assertRaises(RuntimeError):
            diaries.delete("esther", "password")
