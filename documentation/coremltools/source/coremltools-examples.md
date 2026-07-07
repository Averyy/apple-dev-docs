---
source: coremltools
framework: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/coremltools-examples.html
---

# Examples

**

- [.md](../_sources/source/coremltools-examples.md)
- **

.pdf

**

# Examples

 Table of contents 

## Contents

# Examples

The following are code example snippets and full examples of using Core ML Tools to convert models.

## For a Quick Start

Full example:

- [Getting Started](introductory-quickstart.md): Demonstrates how to convert an image classifier model trained using the TensorFlow Keras API to the Core ML format.

## ML Program with Typed Execution

Full example:

- [Typed Execution Workflow Example](typed-execution-example.md): Demonstrates a workflow for checking accuracy using [ML Programs](convert-to-ml-program.md) with [Typed Execution](typed-execution.md).

## TensorFlow 2

- [Load and Convert Model Workflow](load-and-convert-model.md)
- [TensorFlow 2 Workflow](tensorflow-2.md)
- [Convert a Pre-trained Model](tensorflow-2.html#convert-a-pre-trained-model)
- [Convert a User-defined Model](tensorflow-2.html#convert-a-user-defined-model)

Full examples:

- [Getting Started](introductory-quickstart.md): Demonstrates how to convert an image classifier model trained using the TensorFlow Keras API to the Core ML format.
- [Converting TensorFlow 2 BERT Transformer Models](convert-tensorflow-2-bert-transformer-models.md): Converts an object of the tf.keras.Model class and a SavedModel in the TensorFlow 2 format.

## TensorFlow 1

- [Convert From TensorFlow 1](load-and-convert-model.html#convert-from-tensorflow-1).
- [Export as Frozen Graph and Convert](tensorflow-1-workflow.html#export-as-a-frozen-graph-and-convert).
- [Convert a Pre-trained Model](tensorflow-1-workflow.html#convert-a-pre-trained-model).

Full examples:

- [Converting a TensorFlow 1 Image Classifier](convert-a-tensorflow-1-image-classifier.md): Demonstrates the importance of setting the image preprocessing parameters correctly during conversion to get the right results.
- [Converting a TensorFlow 1 DeepSpeech Model](convert-a-tensorflow-1-deepspeech-model.md): Demonstrates automatic handling of flexible shapes using automatic speech recognition.

## PyTorch

- [Convert from PyTorch](load-and-convert-model.html#convert-from-pytorch).
- [PyTorch Conversion Workflow](convert-pytorch-workflow.md).
- [Model Tracing](model-tracing.md).
- [Model Exporting](model-exporting.md).

Full examples:

- [Converting a torchvision Model from PyTorch](convert-a-torchvision-model-from-pytorch.md): Traces / Exports a torchvision MobileNetV2 model, adds preprocessing for image input, and then converts it to Core ML.
- [Converting a PyTorch Segmentation Model](convert-a-pytorch-segmentation-model.md): Converts a PyTorch segmentation model that takes an image and outputs a class prediction for each pixel of the image.
- [Converting an Open Efficient Language Model](convert-openelm.md): Converts a PyTorch [Open Efficient Language Model](https://huggingface.co/apple/OpenELM) to Core ML

## Model Intermediate Language (MIL)

Full example:

- [Model Intermediate Language](model-intermediate-language.md): Construct a MIL program using the Python builder.”

## Conversion Options

### Image Inputs

- [Use an MLMultiArray](image-inputs.html#use-an-mlmultiarray).
- [Use an ImageType](image-inputs.html#use-an-imagetype).
- [Add Image Preprocessing Options](image-inputs.html#add-image-preprocessing-options).

### Classifiers

- [Produce a Classifier Model](classifiers.html#produce-a-classifier-model).

### Flexible Input Shapes

- [Select from Predetermined Shapes](flexible-inputs.html#select-from-predetermined-shapes).
- [Set the Range for Each Dimension](flexible-inputs.html#set-the-range-for-each-dimension).
- [Update a Core ML Model to Use Flexible Input shapes](flexible-inputs.html#update-a-core-ml-model-to-use-flexible-input-shapes)

### Composite and Custom Operators

- [Composite Operators](composite-operators.md): Defining a composite operation by decomposing it into MIL operations.

Full example:

- [Custom Operators](custom-operators.md): Augment Core ML with your own operators and implement them in Swift.

## Optimization

Full examples:

- [Training-Time Compression Examples](https://apple.github.io/coremltools/source/coremltools.optimize.torch.examples.md): Use magnitude pruning, linear quantization, or palettization while training your model, or start from a pre-trained model and fine-tune it with training data.
- [Compressing Neural Network Weights](quantization-neural-network.md): Reduce the size of a neural network by reducing the number of bits that represent a number.

## Trees and Linear Models

- [LibSVM](libsvm-conversion.md)
- [Scikit-learn](sci-kit-learn-conversion.md)
- [XGBoost](xgboost-conversion.md)

## MLModel

### MLModel Overview

- [Load and save the MLModel](mlmodel.html#load-and-save-the-mlmodel).
- [Use the MLModel for Prediction](mlmodel.html#use-the-mlmodel-for-prediction).
- [Work with the Spec](mlmodel.html#work-with-the-spec).
- [Update the Metadata and Input/output Descriptions](mlmodel.html#update-the-metadata-and-input-output-descriptions).

### Model Prediction

- [Make Predictions](model-prediction.md)
- [Multi-array Prediction](model-prediction.html#multi-array-prediction)
- [Image Prediction](model-prediction.html#image-prediction)
- [Image Prediction for a Multi-array Model](model-prediction.html#image-prediction-for-a-multi-array-model)
- [Predict From the Compiled Model](model-prediction.html#predict-from-the-compiled-model)

Full example:

- [Compiled Model Timing Example](model-prediction.html#timing-example): Demonstrates timing differences with calling a large model.

### Xcode Model Preview Types

Full examples:

- [Segmentation Example](xcode-model-preview-types.html#segmentation-example)
- [Body Pose Example](xcode-model-preview-types.html#body-pose-example)

### MLModel Utilities

- [Rename a Feature](mlmodel-utilities.html#rename-a-feature).
- [Convert All Double Multi-array Feature Descriptions to Float](mlmodel-utilities.html#convert-all-double-multi-array-feature-descriptions-to-float).
- [Evaluate Classifier, Regressor, and Transformer models](mlmodel-utilities.html#evaluate-classifier-regressor-and-transformer-models).

## Updatable Models

Full examples:

- [Nearest Neighbor Classifier](updatable-nearest-neighbor-classifier.md): Create an updatable empty k-nearest neighbor.
- [Neural Network Classifier](updatable-neural-network-classifier-on-mnist-dataset.md): Create a simple convolutional model with Keras, convert the model to Core ML, and make the model updatable.
- [Pipeline Classifier](updatable-tiny-drawing-classifier-pipeline-model.md): Use a pipeline composed of a drawing-embedding model and a nearest neighbor classifier to create a model for training a sketch classifier.
If you have a code example you’d like to submit, see [Contributing](how-to-contribute.md).

** Contents
