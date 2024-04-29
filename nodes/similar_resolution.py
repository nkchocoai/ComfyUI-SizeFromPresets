import csv
import os

import torch

import folder_paths
import comfy.model_management

custom_nodes_dir = folder_paths.get_folder_paths("custom_nodes")[0]
presets_dir = os.path.join(custom_nodes_dir, "ComfyUI-SizeFromPresets", "presets")


def load_size_presets(file_name):
    with open(os.path.join(presets_dir, file_name), "r") as f:
        reader = csv.reader(f)
        data = [row for row in reader]
        size_presets = [[int(v.strip()) for v in row] for row in data[1:]]

    return [(w, h, w / h) for w, h in size_presets]


sd15_size_presets = load_size_presets("sd15.csv")
sdxl_size_presets = load_size_presets("sdxl.csv")


def get_similar_resolution(image, size_presets):
    width, height = image[0].shape[1], image[0].shape[0]
    aspect_src = width / height

    similar_res_w, similar_res_h = None, None
    similar_aspect = 10**9
    for w, h, aspect in size_presets:
        if similar_res_w is None:
            similar_res_w = w
        if similar_res_h is None:
            similar_res_h = h

        if abs(aspect - aspect_src) < abs(similar_aspect - aspect_src):
            similar_aspect = aspect
            similar_res_w = w
            similar_res_h = h

    return (similar_res_w, similar_res_h)


class GetSimilarResolution:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "is_sdxl": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("w", "h")

    FUNCTION = "get_size"

    CATEGORY = "SizeFromPresets"

    def get_size(self, image, is_sdxl):
        size_presets = sdxl_size_presets if is_sdxl else sd15_size_presets
        width, height = get_similar_resolution(image, size_presets)
        return (width, height)


class GetSimilarResolutionEmptyLatent:
    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "is_sdxl": ("BOOLEAN", {"default": True}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("latent", "w", "h")

    FUNCTION = "get_size"

    CATEGORY = "SizeFromPresets"

    def get_size(self, image, is_sdxl, batch_size):
        size_presets = sdxl_size_presets if is_sdxl else sd15_size_presets
        width, height = get_similar_resolution(image, size_presets)
        latent = torch.zeros(
            [batch_size, 4, height // 8, width // 8], device=self.device
        )
        return ({"samples": latent}, width, height)
