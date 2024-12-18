from .comfyui_jh_misc_nodes.jh_daisy_chainable_string_constant_node import (
    JHDaisyChainableStringConstantNode,
)

NODE_CLASS_MAPPINGS = {
    "JHDaisyChainableStringConstantNode": JHDaisyChainableStringConstantNode,
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "JHDaisyChainableStringConstantNode": "Daisy-Chainable String Constant",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
