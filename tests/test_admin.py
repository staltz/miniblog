import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from miniblog.admin.models import NUMBER_TWO


class TestLogin:
    def test_dummy(self):
        assert 1+1 == NUMBER_TWO
