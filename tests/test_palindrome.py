from unittest import TestCase

from api.resources.message_resource import is_palindrome


class TestPalindrome(TestCase):

    def test_numbers_as_input(self):
        self.assertFalse(is_palindrome(u'123123023'))

    def test_empty_string(self):
        self.assertFalse(is_palindrome(u''))

    def test_not_unicode(self):
        with self.assertRaises(AssertionError):
            is_palindrome('A but tuba.')

    def test_not_unicode_2(self):
        with self.assertRaises(AssertionError):
            is_palindrome(2)

    def test_punctuation_in_input(self):
        self.assertTrue(
            is_palindrome(
                u'A man, a plan, a cat, a ham, a yak, a yam, a hat, '
                'a canal-Panama!'
            )
        )

    def test_mixed_casing_input(self):
        self.assertTrue(is_palindrome(u'Air An aRIa.'))

    def test_single_letter(self):
        self.assertTrue(is_palindrome(u'A'))
