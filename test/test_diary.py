from unittest import TestCase
from oop.diary.diary import Diary


class Test(TestCase):
    def testthatdiarycanbeunlockedbypasswordwhenlocked(self):
        diary = Diary("username", "password")

        self.assertTrue(diary.is_locked())

        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

    def testthatanexceptionisraisedwhenunlockingwithwrongpassword(self):
        diary = Diary("username", "password")

        with self.assertRaises(RuntimeError):
            diary.unlock_diary("maybe")

    def testdiaryisunlocked_diarycanbelocked(self):
        diary = Diary("username", "password")

        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testthatdiarycancreateentry(self):
        diary = Diary("username", "password")

        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(1, diary.numberofentries())
        self.assertEqual(221, diary.generate_id())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testthatdiarycancreatemorethanoneentry(self):
        diary = Diary("username", "password2")

        diary.unlock_diary("password2")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(221, diary.generate_id())

        diary.create_entry("Title", "Body")
        self.assertEqual(222, diary.generate_id())

        self.assertEqual(2, diary.numberofentries())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testthatdiarycandeleteentry(self):
        diary = Diary("username1", "password1")

        diary.unlock_diary("password1")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(1, diary.numberofentries())
        self.assertEqual(221, diary.generate_id())

        diary.delete_entry(221)
        self.assertEqual(0, diary.numberofentries())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testthatdiarycandeletemorethanoneentry(self):
        diary = Diary("username", "password2")

        diary.unlock_diary("password2")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(221, diary.generate_id())

        diary.create_entry("Title", "Body")
        self.assertEqual(222, diary.generate_id())

        self.assertEqual(2, diary.numberofentries())

        diary.delete_entry(221)
        diary.delete_entry(222)
        self.assertEqual(0, diary.numberofentries())

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testThatAnExceptionIsRaisedWhenTryingToDeleteADeletedEntry(self):
        diary = Diary("username1", "password1")

        diary.unlock_diary("password1")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(1, diary.numberofentries())
        self.assertEqual(221, diary.generate_id())

        diary.delete_entry(221)
        self.assertEqual(0, diary.numberofentries())

        with self.assertRaises(RuntimeError):
            diary.delete_entry(221)

        diary.lock_diary()
        self.assertTrue(diary.is_locked())

    def testthatdiarycanfindentry(self):
        mydiary = Diary("username", "password2")

        mydiary.unlock_diary("password2")
        self.assertFalse(mydiary.is_locked())

        mydiary.create_entry("Title", "Body")
        self.assertEqual(221, mydiary.generate_id())

        mydiary.create_entry("Title", "Body")
        self.assertEqual(222, mydiary.generate_id())

        self.assertEqual(2, mydiary.numberofentries())

        entry1 = mydiary.find_entry(221)
        entry2 = mydiary.find_entry(222)
        self.assertEqual(222, entry2.get_id_no())
        self.assertEqual(221, entry1.get_id_no())

        mydiary.lock_diary()
        self.assertTrue(mydiary.is_locked())

    def testthatanexceptionisraisedwhentryingtofindanentrythatdoesnotexist(self):
        my_diary = Diary("username", "password2")

        my_diary.unlock_diary("password2")
        self.assertFalse(my_diary.is_locked())

        my_diary.create_entry("Title", "Body")
        self.assertEqual(221, my_diary.generate_id())

        with self.assertRaises(RuntimeError):
            my_diary.delete_entry(227)

        my_diary.lock_diary()
        self.assertTrue(my_diary.is_locked())

    def testDiaryIsLocked_ThrowExceptionWhenTryingToCreateEntry(self):
        my_diary = Diary("username", "password2")

        my_diary.lock_diary()
        self.assertTrue(my_diary.is_locked())

        with self.assertRaises(RuntimeError):
            my_diary.create_entry("title", "body")

    def testDiaryIsLocked_ThrowExceptionWhenTryingToDeleteEntry(self):
        my_diary = Diary("username", "password2")

        my_diary.lock_diary()
        self.assertTrue(my_diary.is_locked())

        with self.assertRaises(RuntimeError):
            my_diary.delete_entry(345)

    def testthatdiarycanupdatepreviousentry(self):
        diary = Diary("username", "password2")

        diary.unlock_diary("password2")
        self.assertFalse(diary.is_locked())

        diary.create_entry("Title", "Body")
        self.assertEqual(221, diary.generate_id())

        diary.create_entry("Title", "Body")
        self.assertEqual(222, diary.generate_id())

        self.assertEqual(2, diary.numberofentries())

        diary.update_entry(221, "Title1", "Body1")
        self.assertEqual(2, diary.numberofentries())
        self.assertEqual(0, diary.find_indexof(221))

        diary.update_entry(222, "Title2", "Body2")
        self.assertEqual(2, diary.numberofentries())
        self.assertEqual(1, diary.find_indexof(222))

    def testDiaryIsLocked_ThrowExceptionWhenTryingToUpdateEntry(self):
        my_diary = Diary("username", "password2")

        my_diary.lock_diary()
        self.assertTrue(my_diary.is_locked())

        with self.assertRaises(RuntimeError):
            my_diary.update_entry(222, "title", "body")