import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

import pytest
from person_oop_module import Person



def test_person_initializer_validate_name():
    p1 = Person("John", 36)
    assert p1.name == 'John'

