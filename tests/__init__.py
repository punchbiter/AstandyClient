import unittest

from .syntax_test import BaseTestCase
from .aes_test import AesTestCase
from .communication_test import CommunicationTestCase
from .bolt_test import BoltServiceTestCase
from .player_test import PlayerServiceTestCase

if __name__ == '__main__':
    unittest.main()