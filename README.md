# ComfyUI-SizeFromPresets
![SizeFromPresets Preview](preview.png "SizeFromPresets Preview")  
日本語版READMEは[こちら](README.jp.md)。

- Custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
- Add a node that outputs width and height of the size selected from the preset.

## Installation
```
cd <ComfyUI directory>/custom_nodes
git clone https://github.com/nkchocoai/ComfyUI-SizeFromPresets.git
```

## Nodes
### SizeFromPresets (SD1.5)
- Select image size presets for SD1.5.
- The width and height of the selected size will be output.
- Presets can be set from [presets/sd15.csv](presets/sd15.csv).

### SizeFromPresets (SDXL)
- Select image size presets for SDXL.
- The width and height of the selected size will be output.
- Presets can be set from [presets/sdxl.csv](presets/sdxl.csv).