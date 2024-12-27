# Add the directory containing this file to the Python module search path
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from comfyui_jh_misc_nodes.jh_daisy_chainable_string_constant_node import (
    JHDaisyChainableStringConstantNode,
)
from comfyui_jh_misc_nodes.jh_n_way_switch_node import (
    JHThreeWaySwitchNode,
    JHTwoWaySwitchNode,
)

NODE_CLASS_MAPPINGS = {
    "JHDaisyChainableStringConstantNode": JHDaisyChainableStringConstantNode,
    "JHTwoWaySwitchNode": JHTwoWaySwitchNode,
    "JHThreeWaySwitchNode": JHThreeWaySwitchNode,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "JHDaisyChainableStringConstantNode": "Daisy-Chainable String Constant",
    "JHTwoWaySwitchNode": "Two-Way Switch",
    "JHThreeWaySwitchNode": "Three-Way Switch",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
