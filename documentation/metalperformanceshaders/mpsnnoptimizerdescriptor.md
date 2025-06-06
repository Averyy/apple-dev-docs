# MPSNNOptimizerDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

An object that specifies properties used by an optimizer kernel.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizerDescriptor : NSObject
```

## Topics

### Initializers
- [init(learningRate: Float, gradientRescale: Float, applyGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](mpsnnoptimizerdescriptor/2966726-init.md)
- [init(learningRate: Float, gradientRescale: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](mpsnnoptimizerdescriptor/2966727-init.md)
### Instance Properties
- [var applyGradientClipping: Bool](mpsnnoptimizerdescriptor/2966722-applygradientclipping.md)
- [var gradientClipMax: Float](mpsnnoptimizerdescriptor/2966723-gradientclipmax.md)
- [var gradientClipMin: Float](mpsnnoptimizerdescriptor/2966724-gradientclipmin.md)
- [var gradientRescale: Float](mpsnnoptimizerdescriptor/2966725-gradientrescale.md)
- [var learningRate: Float](mpsnnoptimizerdescriptor/2966728-learningrate.md)
- [var regularizationScale: Float](mpsnnoptimizerdescriptor/2966731-regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](mpsnnoptimizerdescriptor/2966732-regularizationtype.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizer](mpsnnoptimizer.md)
  The base class for optimization layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerdescriptor)*