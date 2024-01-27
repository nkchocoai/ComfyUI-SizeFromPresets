from .nodes.node import *

NODE_CLASS_MAPPINGS = {
    "SizeFromPresetsSD15": SizeFromPresetsSD15,
    "SizeFromPresetsSDXL": SizeFromPresetsSDXL,
    "EmptyLatentImageFromPresetsSD15": EmptyLatentImageFromPresetsSD15,
    "EmptyLatentImageFromPresetsSDXL": EmptyLatentImageFromPresetsSDXL,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeFromPresetsSD15": "Size From Presets (SD1.5)",
    "SizeFromPresetsSDXL": "Size From Presets (SDXL)",
    "EmptyLatentImageFromPresetsSD15": "Empty Latent Image From Presets (SD1.5)",
    "EmptyLatentImageFromPresetsSDXL": "Empty Latent Image From Presets (SDXL)",
}