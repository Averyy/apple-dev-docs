# MPSNNOptimizer

**Framework**: Metal Performance Shaders  
**Kind**: cl

The base class for optimization layers.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNOptimizer : MPSKernel
```

## Topics

### Instance Properties
- [var applyGradientClipping: Bool](mpsnnoptimizer/2966705-applygradientclipping.md)
- [var gradientClipMax: Float](mpsnnoptimizer/2966706-gradientclipmax.md)
- [var gradientClipMin: Float](mpsnnoptimizer/2966707-gradientclipmin.md)
- [var gradientRescale: Float](mpsnnoptimizer/2966708-gradientrescale.md)
- [var learningRate: Float](mpsnnoptimizer/2966709-learningrate.md)
- [var regularizationScale: Float](mpsnnoptimizer/2966710-regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](mpsnnoptimizer/2966711-regularizationtype.md)
### Instance Methods
- [func setLearningRate(Float)](mpsnnoptimizer/2966712-setlearningrate.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
  An optimization layer that performs an Adam pdate.
- [class MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
  An optimization layer that performs a root mean square propagation update.
- [class MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
  An optimization layer that performs a gradient descent with an optional momentum update.
- [class MPSNNOptimizerDescriptor](mpsnnoptimizerdescriptor.md)
  An object that specifies properties used by an optimizer kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizer)*