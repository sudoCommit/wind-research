from src.domain.models.wind_direction import WindDirectionValue
from dataclasses import FrozenInstanceError
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../../')))


class TestWindDirectionValue:
    def test_from_text_valid_direction(self):
        wd = WindDirectionValue.from_text("北東")
        assert wd == WindDirectionValue(
            direction="北東", degree=45.0, original_text="北東")

    def test_from_text_valid_degree(self):
        wd = WindDirectionValue.from_text("180")
        assert wd == WindDirectionValue(
            direction="南", degree=180.0, original_text="180")

    def test_from_text_calm(self):
        wd = WindDirectionValue.from_text("静穏")
        assert wd == WindDirectionValue(
            direction="静穏", degree=-1.0, original_text="静穏")

    def test_from_text_missing(self):
        wd = WindDirectionValue.from_text("///")
        assert wd == WindDirectionValue(
            direction="欠損", degree=-1.0, original_text="///")

    def test_from_text_invalid(self):
        wd = WindDirectionValue.from_text("abc")
        assert wd == WindDirectionValue(
            direction="欠損", degree=-1.0, original_text="abc")

    def test_equality(self):
        wd1 = WindDirectionValue(direction="北", degree=0.0, original_text="北")
        wd2 = WindDirectionValue(direction="北", degree=0.0, original_text="北")
        assert wd1 == wd2

    def test_immutability(self):
        wd = WindDirectionValue(direction="北", degree=0.0, original_text="北")
        with pytest.raises(FrozenInstanceError):
            wd.degree = 90.0
