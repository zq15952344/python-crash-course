import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('jans', 'joplin')
		self.assertEqual(formatted_name, 'jans joplin')

	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('aaa', 'ccc', 'bbb')
		self.assertEqual(formatted_name,'aaa bbb ccc')

unittest.main()