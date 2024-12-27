from typing import Any

from comfyui_jh_misc_nodes import jh_types


class JHTwoWaySwitchNode:
    @classmethod
    def INPUT_TYPES(cls) -> jh_types.JHInputTypesType:
        # fmt: off
        return {
            "required": {},
            "optional":  {
                "input_1": (
                    jh_types.JHAnyType("*"), {}
                ),
                "input_2": (
                    jh_types.JHAnyType("*"), {}
                ),
            },
            "hidden": {},
        }
        # fmt: on

    RETURN_TYPES = (jh_types.JHAnyType("*"),)
    FUNCTION = "two_way_switch"
    CATEGORY = "JH Misc Nodes"
    OUTPUT_NODE = False
    EXPERIMENTAL = True

    # It's generally bad practice to use `Any` this way, but in this case we
    # have to because the inputs and outputs can literally be any data type.
    def two_way_switch(self, input_1: Any = None, input_2: Any = None) -> Any:  # noqa: ANN401
        if input_1 is not None:
            return (input_1,)

        if input_2 is not None:
            return (input_2,)

        return (None,)
