---
source: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/opt-palettization-perf.html
---

# Performance

**

- [.md](../_sources/source/opt-palettization-perf.md)
- **

.pdf

**

# Performance

 Table of contents 

## Contents

# Performance

Since palettization reduces the size of each weight value, the amount of data to be moved is reduced during prediction.
This can lead to benefits in memory-bottlenecked models. Note that this latency advantage is available only when
palettized weights are loaded and are decompressed “just in time” for computation. Starting with `iOS17/macOS14`, this is
more likely to happen for models running primarily on the Neural Engine backend.

For the `per_grouped_channel` palettization mode added in `iOS18/macOS15`, you may see a drop in runtime performance as
the number of LUTs used to represent a weight tensor increases. Typically, a group size of 8 or 16 gives good accuracy while still increasing speed over an uncompressed model.

## Performance Benchmarks

In the table below, we provide runtime performance benchmarks on several models, palettized using `coremltools.optimize` APIs.

### Methodology

The training time compressed models were obtained by fine-tuning the `float32` PyTorch models with weights initialized from the checkpoints linked in the [Model Info](#model-info) table, and using methods from `coremltools.optimize.torch` to perform compression. The datasets used for fine-tuning the models are also linked in the same table, along with the accuracy metric being reported. We used fine-tuning recipes which are commonly used in literature for the task at hand and for standard data augmentations.

Similarly, the post training compressed models were obtained by compressing the converted `float16` Core ML models, with pre-trained weights, using methods from the `coremltools.optimize.coreml` module.

The trained and compressed models and the `coremltools.optimize.torch` config files used for compression can be downloaded by clicking the respective links embedded in the model and config names.

The latency numbers were captured using the Xcode **Performance** tab, using the `median` statistic. Compute unit selection is `all` unless otherwise noted. The latency numbers are sensitive to the device state, and may vary depending on the device state and build versions.

- Device: iPhone 14 Pro (A16), unless otherwise mentioned
- iOS build: iOS17
- Xcode : Xcode 15

### Model Info

| Model Name | Task | Pre-trained Weights | Dataset | Accuracy Metric |
| --- | --- | --- | --- | --- |
| MobileNetv2-1.0 | Image Classification | Torchvision | ImageNet | Top-1 Accuracy (%) |
| MobileNetv3-small | Image Classification | Torchvision | ImageNet | Top-1 Accuracy (%) |
| ResNet50 | Image Classification | Torchvision | ImageNet | Top-1 Accuracy (%) |
| MobileViTv2-1.0 | Image Classification | cvnets | ImageNet | Top-1 Accuracy (%) |
| CenterNet (ResNet34 backbone) | Object Detection | Torchvisionbackbone | MS-COCO | mAP |

### Results

| Model Name | Config | Optimization Algorithm | Compression Ratio | Latency in ms (per batch) |
| --- | --- | --- | --- | --- |
| MobileNetv2-1.0 | Float16 | n/a | 1.0 | 0.48 |
| MobileNetv2-1.0 | 2 bit | Differentiable K-Means | 5.92 | 0.47 |
| MobileNetv2-1.0 | 4 bit | Differentiable K-Means | 3.38 | 0.45 |
| MobileNetv2-1.0 | 6 bit | K-Means | 2.54 | 0.48 |
| MobileNetv2-1.0 | 8 bit | K-Means | 1.97 | 0.45 |
| MobileNetv3-small | Float16 | n/a | 1.0 | 0.13 |
| MobileNetv3-small | 2 bit | Differentiable K-Means | 5.82 | 0.13 |
| MobileNetv3-small | 4 bit | Differentiable K-Means | 3.47 | 0.13 |
| MobileNetv3-small | 6 bit | K-Means | 2.6 | 0.13 |
| MobileNetv3-small | 8 bit | K-Means | 1.93 | 0.13 |
| ResNet50 | Float16 | n/a | 1.0 | 1.52 |
| ResNet50 | 2 bit | Differentiable K-Means | 7.63 | 1.43 |
| ResNet50 | 4 bit | Differentiable K-Means | 3.9 | 1.41 |
| ResNet50 | 6 bit | K-Means | 2.65 | 1.37 |
| ResNet50 | 8 bit | K-Means | 1.99 | 1.4 |
| CenterNet (ResNet34 backbone) | Float16 | n/a | 1.0 | 6.85 |
| CenterNet (ResNet34 backbone) | 2 bit | Differentiable K-Means | 7.71 | 6.37 |
| CenterNet (ResNet34 backbone) | 4 bit | Differentiable K-Means | 3.94 | 6.67 |
| CenterNet (ResNet34 backbone) | 6 bit | K-Means | 2.65 | 6.71 |
| CenterNet (ResNet34 backbone) | 8 bit | K-Means | 2.0 | 6.85 |

** Contents
