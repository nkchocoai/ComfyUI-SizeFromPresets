import csv
import os

import torch

import folder_paths

import comfy.model_management

custom_nodes_dir = folder_paths.get_folder_paths("custom_nodes")[0]
presets_dir = os.path.join(custom_nodes_dir, "ComfyUI-SizeFromPresets", "presets")

def load_size_presets_input(file_name,digit):
    with open(os.path.join(presets_dir, file_name),'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]
        size_presets = [[int(v.strip()) for v in row] for row in data[1:]]

    return [f'{w: >{digit}} x {h: >{digit}}' for w,h in size_presets]
    
class SizeFromPresetsBase:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (cls.SIZE_PRESETS_INPUT,),
            }
        }

    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("w","h")

    FUNCTION = "get_size"

    CATEGORY = "SizeFromPresets"

    def get_size(self, preset):
        parsed_preset = [int(v.strip()) for v in preset.split('x')]
        return (parsed_preset[0], parsed_preset[1])
    
class SizeFromPresetsSD15(SizeFromPresetsBase):
    SIZE_PRESETS_INPUT = load_size_presets_input('sd15.csv',3)
    
class SizeFromPresetsSDXL(SizeFromPresetsBase):
    SIZE_PRESETS_INPUT = load_size_presets_input('sdxl.csv',4)

class EmptyLatentImageFromPresetsBase:
    def __init__(self):
        self.device = comfy.model_management.intermediate_device()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { 
                "preset": (cls.SIZE_PRESETS_INPUT,),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096})
            }
        }
    RETURN_TYPES = ("LATENT","INT","INT")
    RETURN_NAMES = ("latent","w","h")
    FUNCTION = "generate"

    CATEGORY = "SizeFromPresets"

    def generate(self, preset, batch_size=1):
        w,h = [int(v.strip()) for v in preset.split('x')]
        latent = torch.zeros([batch_size, 4, h // 8, w // 8], device=self.device)
        return ({"samples":latent}, w, h)
    
class EmptyLatentImageFromPresetsSD15(EmptyLatentImageFromPresetsBase):
    SIZE_PRESETS_INPUT = load_size_presets_input('sd15.csv',3)
    
class EmptyLatentImageFromPresetsSDXL(EmptyLatentImageFromPresetsBase):
    SIZE_PRESETS_INPUT = load_size_presets_input('sdxl.csv',4)