from __future__ import absolute_import
import unittest
import os
from firemansam import functions as firemansam


class FiremanTests(unittest.TestCase):

    def test_firedict(self):

        filename = os.path.abspath(os.path.dirname(__file__)) + '/py2example'
        pyfilename = filename + '.py'
        os.rename(filename, pyfilename)

        result = firemansam.firedict(pyfilename)

        os.rename(pyfilename, filename)

        expected = {'file': pyfilename, 'scale': 1}

        self.assertEqual(expected, result)

        filename = os.path.abspath(os.path.dirname(__file__)) + '/py3example'
        pyfilename = filename + '.py'
        os.rename(filename, pyfilename)

        result = firemansam.firedict(pyfilename)

        os.rename(pyfilename, filename)

        expected = {'file': pyfilename, 'scale': 0}

        self.assertEqual(expected, result)
