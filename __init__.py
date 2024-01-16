from .nodes.node import *

NODE_CLASS_MAPPINGS = {
    "SizeFromPresetsSD15": SizeFromPresetsSD15,
    "SizeFromPresetsSDXL": SizeFromPresetsSDXL,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeFromPresetsSD15": "SizeFromPresets (SD1.5)",
    "SizeFromPresetsSDXL": "SizeFromPresets (SDXL)",
}