---
source: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/opt-whats-new.html
---

# What’s New

**

- [.md](../_sources/source/opt-whats-new.md)
- **

.pdf

**

# What’s New

 Table of contents 

## Contents

# What’s New

## Software Availability of Optimizations

| OS version | Compression modes or optimizations added |
| --- | --- |
| iOS16/macOS13 | * Palettization:* per-tensor LUT* {1,2,4,6,8} bits of compression* Quantization:* 8-bit* weight only* per-channel scales/offsets* Pruning* Support via ahead-of-runtime weight decompression tofloat16 |
| iOS17/macOS14 | * Quantization:* activation quantization (W8A8 mode), accelerated on NE for A17 pro/M4 chips* Updated faster compression kernels, decompression “on the fly” for some cases |
| iOS18/macOS15 | * Palettization:* per-grouped channel LUTs* 3-bit compression* INT8 LUTs* per-channel scale option with LUT* Quantization:* 4-bit weight* per-block scales/offsets* Pruning* palettization of non-zero values* quantization of non-zero values |

Optimizations for iOS15 / macOS12 and lower

Compression optimizations can only be applied to
the `neuralnetwork` model type.
This can be done via the `ct.models.neural_networks.quantization_utils.*` APIs.

For later OS versions, all optimizations are applicable to the `mlprogram` model
type only and can be accessed via the APIs available
under the `coremltools.optimize.*` subspace.

## Core ML Tools Optimization APIs

The following sections contain a list of APIs available in coremltools to transform models using
different compression modes (mentioned in the table above) and [workflows](opt-workflow.md).
Note that `coremltools.optimize` is denoted as `cto` below.

### Core ML Tools 8

All previous (coremltools 7) APIs have been updated to support
new compression modes available in `iOS18` / `macOS15` (e.g. grouped channel palettization).
The following APIs have also been added, available from `coremltools==8.0b1`:

| Compression Type | Input Model format | API (method or class) | Optimization workflow |
| --- | --- | --- | --- |
| Palettization | PyTorch model | cto.torch.palettization.PostTrainingPalettizer | palettize in a data-free manner |
| Palettization | PyTorch model | cto.torch.palettization.SKMPalettizer | palettize with calibration dataset using sensitive k-means algorithm |
| Quantization | PyTorch model | cto.torch.layerwise_compression | quantize with calibration dataset using the GPTQ algorithm |
| Quantization | PyTorch model | cto.torch.quantization.PostTrainingQuantizer | quantize weights in a data-free manner |
| Pruning | PyTorch model | cto.torch.layerwise_compression | prune with calibration dataset using the SparseGPT algorithm |

Another method, `cto.coreml.experimental.linear_quantize_activations`,
takes an `mlpackage` and calibration data
and produces a model with activations quantized
to 8 bits. This can then be passed to the `cto.coreml.linear_quantize_weights` method
to get a W8A8 model. The API and its implementations may undergo some changes as it is moved out of the experimental namespace
in future non-beta releases of Core ML Tools.

### Core ML Tools 7

| Compression Type | Input Model format | API (method or class) | Optimization workflow |
| --- | --- | --- | --- |
| Palettization | Core ML (mlpackage) | cto.coreml.palettize_weights | palettize in a data-free manner |
| Palettization | PyTorch model | cto.torch.palettization.DKMPalettizer | palettize via fine-tuning using differentiable k-means |
| Quantization | Core ML (mlpackage) | cto.coreml.linear_quantize_weights | quantize weights to 8 bits in a data-free manner |
| Quantization | PyTorch model | cto.torch.quantization.LinearQuantizer | quantize weights and/or activations either with fine-tuning or with a calibration dataset |
| Pruning | Core ML (mlpackage) | cto.coreml.prune_weights | transform a dense model to one with sparse weights |
| Pruning | PyTorch model | cto.torch.pruning.MagnitudePruner | sparsify via fine-tuning using magnitude-based pruning algorithm |

** Contents
