"""Tests if  ``is_float`` is working as expected

--------------------------------------------------------------------------------
Command to run at the prompt:
    python -m unittest -v tests/types/test_is_float.py
--------------------------------------------------------------------------------
"""

### GENERAL IMPORTS ###
import os
import unittest
import numpy as np


### FUNCTION IMPORT ###
from paramcheckup.types import is_float


os.system("cls")


class Test_is_float(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = 0.05
        cls.param_name = "alpha"
        cls.kind = "function"
        cls.kind_name = "ttest"
        cls.stacklevel = 3
        cls.error = True
        cls.values = [
            "anderson",
            1,
            np.int32(1),
            np.int64(1),
            [1],
            [[1]],
            (1,),
            (1, 1, 1),
            (1, (1,), 1),
            None,
            {"a": 1},
            set([1, 2, 3]),
        ]

    def test_outputs(self):
        output = is_float(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

        output = is_float(
            value=self.value,
            param_name=self.param_name,
            kind=self.kind,
            kind_name=self.kind_name,
            stacklevel=self.stacklevel,
            error=self.error,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_pass_erro_ffalse(self):
        output = is_float(
            self.value,
            self.param_name,
            self.kind,
            self.kind_name,
            self.stacklevel,
            False,
        )
        self.assertTrue(output, msg="not True when must be True")

    def test_raises(self):
        for value in self.values:
            with self.assertRaises(
                TypeError,
                msg=f"Does not raised error when value is a {type(value).__name__}",
            ):
                output = is_float(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=self.error,
                )

    def test_raises_error_false(self):
        for value in self.values:
            with self.assertRaises(
                SystemExit,
                msg=f"Does not raised SystemExit when value is a {type(value).__name__}",
            ):
                output = is_float(
                    value=value,
                    param_name=self.param_name,
                    kind=self.kind,
                    kind_name=self.kind_name,
                    stacklevel=self.stacklevel,
                    error=False,
                )


if __name__ == "__main__":
    unittest.main()
