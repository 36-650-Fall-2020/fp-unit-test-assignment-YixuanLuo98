import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join (parent_dir, "src")
sys.path.insert(0,src_dir)

import pytest
from word_counter_fp_module import *

def test_count_words_validate_length():
    assert len(count_words(use_state_data_file())) > 0

