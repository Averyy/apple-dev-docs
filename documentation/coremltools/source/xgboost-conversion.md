---
source: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/xgboost-conversion.html
---

# XGBoost

**

- [.md](../_sources/source/xgboost-conversion.md)
- **

.pdf

**

# XGBoost

 Table of contents 

# XGBoost

You can convert a trained [XGBoost](https://en.wikipedia.org/wiki/XGBoost) model to Core ML format using [xgboost.convert()](https://apple.github.io/coremltools/source/coremltools.converters.xgboost.html#coremltools.converters.xgboost._tree.convert):

```
# Convert it with default input and output names
import coremltools as ct
coreml_model = ct.converters.xgboost.convert(model)

# Saving the Core ML model to a file.
coreml_model.save('my_model.mlmodel')
```

For more information, see the [API Reference](https://apple.github.io/coremltools/source/coremltools.converters.xgboost.html#module-coremltools.converters.xgboost._tree).
