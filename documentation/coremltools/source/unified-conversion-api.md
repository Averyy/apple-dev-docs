---
source: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/unified-conversion-api.html
---

# Core ML Tools API Overview

**

- [.md](../_sources/source/unified-conversion-api.md)
- **

.pdf

**

# Core ML Tools API Overview

 Table of contents 

# Core ML Tools API Overview

Core ML Tools is the [coremltools](https://apple.github.io/coremltools/index.md) Python package for macOS (10.13+) and Linux. It includes the [Unified Conversion API](https://apple.github.io/coremltools/source/coremltools.converters.convert.html#module-coremltools.converters._converters_entry) for converting deep learning models and neural networks to [Core ML](https://developer.apple.com/documentation/coreml).

For example, you can use the Unified Conversion API to convert TensorFlow and PyTorch source model frameworks to Core ML. For the conversion parameters, see the [convert()](https://apple.github.io/coremltools/source/coremltools.converters.convert.html#coremltools.converters._converters_entry.convert) method.

Note

This section is about converting neural network models using the Unified Conversion API. For converting other classic models, see [LibSVM](libsvm-conversion.md), [Scikit-learn](sci-kit-learn-conversion.md), and [XGBoost](xgboost-conversion.md) in the “Other Converters” section.

For instructions and examples, see the following pages:

- [Converting Deep Learning Models](convert-learning-models.md)
- [ML Programs](convert-to-ml-program.md)
- [Converting from PyTorch](convert-pytorch.md)
- [Converting from TensorFlow](convert-tensorflow.md)
- [Examples](coremltools-examples.md)

For common scenarios using conversion options, see the following pages:

- [Model Input and Output Types](model-input-and-output-types.md)
- [Image Input and Output](image-inputs.md)
- [Classifiers](classifiers.md)
- [Flexible Input Shapes](flexible-inputs.md)
- [Composite Operators](composite-operators.md)
- [Custom Operators](custom-operators.md)
- [Graph Passes](graph-passes-intro.md)
