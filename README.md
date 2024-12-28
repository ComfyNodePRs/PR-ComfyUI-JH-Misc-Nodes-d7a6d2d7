![image](https://github.com/user-attachments/assets/90e7c8f5-ef7c-41ab-a676-85f0b77d9b55)


# JH Misc. Nodes

![GitHub License](https://img.shields.io/github/license/ComfyUI-JH/ComfyUI_JH_Misc_Nodes)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/jefferyharrell/ComfyUI_JH_Misc_Nodes/ci.yml)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/ComfyUI-JH/ComfyUI_JH_Misc_Nodes/main)

Miscellaneous custom nodes for ComfyUI that I made for my own use. Figured I might as well share.

# Getting Started

## Installing from GitHub

1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

2. Clone this repository into the `custom_nodes` folder:

    ```
    cd ComfyUI/custom_nodes
    git clone https://github.com/ComfyUI-JH/ComfyUI_JH_Misc_Nodes.git
    ```

3. Install the required Python packages. If you're using `venv` and `pip` that looks like this:

    ```
    cd ComfyUI_JH_Misc_Nodes
    pip install -r requirements.txt
    ```

    If you're using [Poetry](https://python-poetry.org/), then it's just

    ```
    cd ComfyUI_JH_Misc_Nodes
    poetry install
    ```

# Nodes

## Daisy-Chainable String Constant

<div align="center">
    <img width="1391" alt="image" src="https://github.com/user-attachments/assets/77b0b3db-63da-4687-9029-59554a0fb0ac" />
</div>

A node with a text input and a text widget. Any text typed into the widget will be stripped of excess whitespace and concatenated onto the end of the input text. Useful for breaking a prompt into pieces which can be edited independently.

## Preview Image

<div align="center">
    <img width="450" alt="image" src="https://github.com/user-attachments/assets/a1a5cdc8-20ee-4f0f-9e00-b97e5ce7cad0" />
</div>

Takes an image or batch of images as an input, displays a preview of them, then passes them along to the output.

