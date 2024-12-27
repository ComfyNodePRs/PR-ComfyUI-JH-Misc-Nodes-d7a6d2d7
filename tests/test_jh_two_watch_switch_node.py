import pytest

from comfyui_jh_misc_nodes.jh_two_way_switch_node import JHTwoWaySwitchNode


@pytest.fixture
def node() -> JHTwoWaySwitchNode:
    return JHTwoWaySwitchNode()


def test_two_way_switch_node_none_none(node: JHTwoWaySwitchNode) -> None:
    assert node.two_way_switch(None, None) == (None,)


def test_two_way_switch_node_none_value(node: JHTwoWaySwitchNode) -> None:
    assert node.two_way_switch(None, "value") == ("value",)


def test_two_way_switch_node_value_none(node: JHTwoWaySwitchNode) -> None:
    assert node.two_way_switch("value", None) == ("value",)
