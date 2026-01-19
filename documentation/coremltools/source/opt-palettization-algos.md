---
source: coremltools
framework: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/opt-palettization-algos.html
---

# Palettization Algorithms

**

- [.md](../_sources/source/opt-palettization-algos.md)
- **

.pdf

**

# Palettization Algorithms

 Table of contents 

## Contents

# Palettization Algorithms

There are a few different ways in which a model’s weights can be palettized.
For the same compression factor, each of these approaches can have a different impact on model accuracy.
Below we talk about different palettization algorithms that are supported, and some of the considerations to keep in mind when choosing the approach that works well for your use case.

## K-Means

This is a data-free post-training palettization algorithm where weights are clustered using [k-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) and where the derived centroids form the lookup table (LUT).
Since this only requires model weights, it is the easiest algorithm to set up and experiment with. For higher bit palettization, post-training palettization provides a good compression-accuracy tradeoff.
However, there is a significant loss in accuracy for lower bits. For lower bits, `per_grouped_channel` granularity can be used to recover the loss in accuracy.

Supported API(s):

- [coremltools.optimize.coreml.palettize_weights](https://apple.github.io/coremltools/source/coremltools.optimize.coreml.post_training_quantization.html#coremltools.optimize.coreml.palettize_weights)
- [coremltools.optimize.torch.palettization.PostTrainingPalettizer](https://apple.github.io/coremltools/source/coremltools.optimize.torch.palettization.html#coremltools.optimize.torch.palettization.PostTrainingPalettizer)

## Sensitive K-Means

Sensitive K-Means is a calibration data based post-training palettization algorithm, based on [SqueezeLLM: Dense-and-Sparse Quantization](https://arxiv.org/pdf/2306.07629).
It palettizes weights by running a weighted k-means on model parameters. These weights, called sensitivity, are computed
using an objective function that depends on the Hessian of the model parameters. Since Hessian is a second-order derivative and computationally expensive to calculate,
it is approximated by using the Fisher information matrix, which is computed from the square of gradients easily available given a few calibration input data points
and a loss function.

The more sensitive an element, the larger impact perturbing it (in this case, palettizing it) has on the model’s loss function.
Thus, weighted k-means moves the clusters closer to the sensitive weight values, allowing them to be represented more precisely. This generally leads to lower degradation in model accuracy but depends on model type and how accurate the Fisher Information approximation is for that specific model.
Typically, 128 samples are sufficient for applying this algorithm. In practice, this algorithm works well, better than data-free K-Means, for large transformer-based architectures.

Supported API(s):

- [coremltools.optimize.torch.palettization.SKMPalettizer](https://apple.github.io/coremltools/source/coremltools.optimize.torch.palettization.html#coremltools.optimize.torch.palettization.SKMPalettizer)

## Differentiable K-Means

[Differentiable K-means (DKM)](https://arxiv.org/abs/2108.12659) is a training time palettization algorithm.
The key idea of the algorithm is that in each training step, a soft k-means cluster assignment of weight tensors is performed such that each operation in the process is differentiable.
This allows for gradient updates to take place for the weights while a lookup table (LUT) of centroids and indices are learned.
This is achieved by inserting palettization submodules inside a model, which simulate palettization during training using the differentiable version of the k-means algorithm.
This algorithm provides the best compression-accuracy tradeoff across all algorithms and can be used with very low bit precisions, while still retaining good accuracy.
However, this is also the most time and data intensive. Since the algorithm involves computation of the distance and the attention matrices, in practice it can also take substantial memory.

Supported API(s):

- [coremltools.optimize.torch.palettization.DKMPalettizer](https://apple.github.io/coremltools/source/coremltools.optimize.torch.palettization.html#coremltools.optimize.torch.palettization.DKMPalettizer)

## Methodology

In the tables below, we provide accuracy benchmarks on several models, palettized using `coremltools.optimize` APIs.

See [Palettization Performance](opt-palettization-perf.md) page to learn more about how the benchmarked models were generated.

All evaluations were performed on the final compressed (or uncompressed) CoreML models, using the validation subset of the dataset linked in [Model Info](opt-palettization-perf.html#model-info). The training time compressed models were trained for three trials, starting from the same pre-trained weights, and using a different ordering of data during training for each trial. For these models, we report the mean accuracy across the three trials, along with the standard deviation.

## Results

| Model Name | Config | Optimization Algorithm | Compression Ratio | Accuracy |
| --- | --- | --- | --- | --- |
| MobileNetv2-1.0 | Float16 | n/a | 1.0 | 71.86 |
| MobileNetv2-1.0 | 2 bit | Differentiable K-Means | 5.92 | 68.81 ± 0.04 |
| MobileNetv2-1.0 | 4 bit | Differentiable K-Means | 3.38 | 70.60 ± 0.08 |
| MobileNetv2-1.0 | 6 bit | K-Means | 2.54 | 70.89 |
| MobileNetv2-1.0 | 8 bit | K-Means | 1.97 | 71.80 |
| MobileNetv3-small | Float16 | n/a | 1.0 | 67.58 |
| MobileNetv3-small | 2 bit | Differentiable K-Means | 5.82 | 59.82 ± 0.98 |
| MobileNetv3-small | 4 bit | Differentiable K-Means | 3.47 | 67.23 ± 0.04 |
| MobileNetv3-small | 6 bit | K-Means | 2.6 | 65.46 |
| MobileNetv3-small | 8 bit | K-Means | 1.93 | 67.44 |
| ResNet50 | Float16 | n/a | 1.0 | 76.14 |
| ResNet50 | 2 bit | Differentiable K-Means | 7.63 | 75.47 ± 0.05 |
| ResNet50 | 4 bit | Differentiable K-Means | 3.9 | 76.63 ± 0.01 |
| ResNet50 | 6 bit | K-Means | 2.65 | 75.68 |
| ResNet50 | 8 bit | K-Means | 1.99 | 76.05 |
| CenterNet (ResNet34 backbone) | Float16 | n/a | 1.0 | 29.0 |
| CenterNet (ResNet34 backbone) | 2 bit | Differentiable K-Means | 7.71 | 25.66 ± 0.03 |
| CenterNet (ResNet34 backbone) | 4 bit | Differentiable K-Means | 3.94 | 28.14 ± 0.11 |
| CenterNet (ResNet34 backbone) | 6 bit | K-Means | 2.65 | 28.27 |
| CenterNet (ResNet34 backbone) | 8 bit | K-Means | 2.0 | 28.75 |

** Contents
