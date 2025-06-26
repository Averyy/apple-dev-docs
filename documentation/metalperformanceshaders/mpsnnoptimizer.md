# MPSNNOptimizer

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSNNOptimizer
```

## Topics

### Instance Properties
- [var applyGradientClipping: Bool](mpsnnoptimizer/applygradientclipping.md)
- [var gradientClipMax: Float](mpsnnoptimizer/gradientclipmax.md)
- [var gradientClipMin: Float](mpsnnoptimizer/gradientclipmin.md)
- [var gradientRescale: Float](mpsnnoptimizer/gradientrescale.md)
- [var learningRate: Float](mpsnnoptimizer/learningrate.md)
- [var regularizationScale: Float](mpsnnoptimizer/regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](mpsnnoptimizer/regularizationtype.md)
### Instance Methods
- [func setLearningRate(Float)](mpsnnoptimizer/setlearningrate(_:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSNNOptimizerAdam](mpsnnoptimizeradam.md)
- [MPSNNOptimizerRMSProp](mpsnnoptimizerrmsprop.md)
- [MPSNNOptimizerStochasticGradientDescent](mpsnnoptimizerstochasticgradientdescent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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