from .nodes.node import *
from .nodes.random import *
from .nodes.similar_resolution import *

NODE_CLASS_MAPPINGS = {
    "SizeFromPresetsSD15": SizeFromPresetsSD15,
    "SizeFromPresetsSDXL": SizeFromPresetsSDXL,
    "EmptyLatentImageFromPresetsSD15": EmptyLatentImageFromPresetsSD15,
    "EmptyLatentImageFromPresetsSDXL": EmptyLatentImageFromPresetsSDXL,
    "RandomSizeFromPresetsSD15": RandomSizeFromPresetsSD15,
    "RandomSizeFromPresetsSDXL": RandomSizeFromPresetsSDXL,
    "RandomEmptyLatentImageFromPresetsSD15": RandomEmptyLatentImageFromPresetsSD15,
    "RandomEmptyLatentImageFromPresetsSDXL": RandomEmptyLatentImageFromPresetsSDXL,
    "GetSimilarResolution": GetSimilarResolution,
    "GetSimilarResolutionEmptyLatent": GetSimilarResolutionEmptyLatent,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeFromPresetsSD15": "Size From Presets (SD1.5)",
    "SizeFromPresetsSDXL": "Size From Presets (SDXL)",
    "EmptyLatentImageFromPresetsSD15": "Empty Latent Image From Presets (SD1.5)",
    "EmptyLatentImageFromPresetsSDXL": "Empty Latent Image From Presets (SDXL)",
    "RandomSizeFromPresetsSD15": "Random Size From Presets (SD1.5)",
    "RandomSizeFromPresetsSDXL": "Random Size From Presets (SDXL)",
    "RandomEmptyLatentImageFromPresetsSD15": "Random Empty Latent Image From Presets (SD1.5)",
    "RandomEmptyLatentImageFromPresetsSDXL": "Random Empty Latent Image From Presets (SDXL)",
    "GetSimilarResolution": "Get Similar Resolution",
    "GetSimilarResolutionEmptyLatent": "Get Similar Resolution Empty Latent",
}
