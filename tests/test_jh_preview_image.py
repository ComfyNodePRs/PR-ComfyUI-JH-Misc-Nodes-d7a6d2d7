import pytest

from comfyui_jh_misc_nodes.jh_preview_image import JHPreviewImage


@pytest.fixture
def node() -> JHPreviewImage:
    return JHPreviewImage()
