import unittest
import os
from firemansam.firedict import firedict


class FiremanTests(unittest.TestCase):

    def test_firedict(self):

        py2file = 'py2example'
        try:
            filename = os.path.abspath(os.path.dirname(__file__)) + '/' + py2file
            py2filename = filename + '.py'
            os.rename(filename, py2filename)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            result = firedict(py2filename)
            os.rename(py2filename, filename)
            expected = {'file': py2filename, 'scale': 1}
            self.assertEqual(expected, result)

        py3file = 'py3example'
        try:
            filename = os.path.abspath(os.path.dirname(__file__)) + '/' + py3file
            py3filename = filename + '.py'
            os.rename(filename, py3filename)
        except OSError as err:
            print("OS error: {0}".format(err))
        else:
            result = firedict(py3filename)
            os.rename(py3filename, filename)
            expected = {'file': py3filename, 'scale': 0}
            self.assertEqual(expected, result)
