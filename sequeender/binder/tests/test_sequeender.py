#!/usr/bin/env python3

import pytest

from sequeender import sequeender


def test_sequeender_widget():
    w = sequeender.SequeenderWidget(-3)
    assert w.get() == -3


@pytest.mark.parametrize(
    "member_t, member_val", [(int, 1), (float, 3.1), (bool, False)]
)
def test_sequeender_gadget(member_t, member_val):
    g = sequeender.SequeenderGadget[member_t](member_val)
    assert g.get() == pytest.approx(member_val)
