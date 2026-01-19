---
source: coremltools
framework: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html
---

# What Is Core ML Tools?

**

- [.md](../_sources/source/overview-coremltools.md)
- **

.pdf

**

# What Is Core ML Tools?

 Table of contents 

## Contents

# What Is Core ML Tools?

The [coremltools](https://github.com/apple/coremltools) Python package is the primary way to convert third-party models to Core ML. [Core ML](https://developer.apple.com/documentation/coreml) is an Apple framework to integrate machine learning models into your app.

For details about using the `coremltools` API classes and methods, see the [coremltools API Reference](https://apple.github.io/coremltools/index.md).

Use Core ML Tools to convert models from third-party training libraries such as [TensorFlow](https://www.tensorflow.org) and [PyTorch](https://pytorch.org) to the [Core ML model package format](https://developer.apple.com/documentation/coreml/core_ml_api/updating_a_model_file_to_a_model_package). You can then use Core ML to integrate the models into your app.

![Core ML Tools overview](../_images/introduction-coremltools.png)

Convert a third-party model to a Core ML model package file.

With Core ML Tools you can:

- Convert trained models from libraries and frameworks such as [TensorFlow](https://www.tensorflow.org) and [PyTorch](https://pytorch.org) to the Core ML model package format.
- Read, write, and optimize Core ML models to use less storage space, reduce power consumption, and reduce latency during inference.
- Verify creation and conversion by making predictions using Core ML in macOS.

Core ML provides a unified representation for all models. Your app uses Core ML APIs and user data to make predictions, and to fine-tune models, all on the user’s device. Running a model strictly on the user’s device removes any need for a network connection, which helps keep the user’s data private and your app responsive.

Core ML optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine (NE) while minimizing its memory footprint and power consumption.

## Additional Resources

- The [coremltools API Reference](https://apple.github.io/coremltools/index.md) provides details about using the `coremltools` API classes and methods.
- The [Machine Learning](https://developer.apple.com/machine-learning/) page provides educational material, tutorials, guides, and documentation for Apple developers.
- The [ML & Vision session videos](https://developer.apple.com/videos/frameworks/machine-learning-and-vision) from the World Wide Developer Conference are a great place to start if you are new to machine learning technology and Core ML.
- The [Core ML documentation](https://developer.apple.com/documentation/coreml) walks you through the first steps in developing an app with a machine learning model.
- Try out `coremltools` in your browser with Binder: [](https://mybinder.org/v2/gh/ContinuumIO/coreml-demo/HEAD)

## Supported Libraries and Frameworks

You can convert trained models from the following libraries and frameworks to Core ML:

| Model Family | Supported Packages |
| --- | --- |
| Neural Networks | TensorFlow 1 (1.14.0+),TensorFlow 2 (2.1.0+),PyTorch (1.13.0+) |
| Tree Ensembles | XGboost (1.1.0),scikit-learn (0.18.1) |
| Generalized Linear Models | scikit-learn (0.18.1) |
| Support Vector Machines | LIBSVM (3.22),scikit-learn (0.18.1) |
| Pipelines (pre- and post-processing) | scikit-learn (0.18.1) |

** Contents
