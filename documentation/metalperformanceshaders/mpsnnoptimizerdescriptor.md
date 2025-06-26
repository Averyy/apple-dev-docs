# MPSNNOptimizerDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSNNOptimizerDescriptor
```

## Topics

### Initializers
- [init(learningRate: Float, gradientRescale: Float, applyGradientClipping: Bool, gradientClipMax: Float, gradientClipMin: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](mpsnnoptimizerdescriptor/init(learningrate:gradientrescale:applygradientclipping:gradientclipmax:gradientclipmin:regularizationtype:regularizationscale:).md)
- [init(learningRate: Float, gradientRescale: Float, regularizationType: MPSNNRegularizationType, regularizationScale: Float)](mpsnnoptimizerdescriptor/init(learningrate:gradientrescale:regularizationtype:regularizationscale:).md)
### Instance Properties
- [var applyGradientClipping: Bool](mpsnnoptimizerdescriptor/applygradientclipping.md)
- [var gradientClipMax: Float](mpsnnoptimizerdescriptor/gradientclipmax.md)
- [var gradientClipMin: Float](mpsnnoptimizerdescriptor/gradientclipmin.md)
- [var gradientRescale: Float](mpsnnoptimizerdescriptor/gradientrescale.md)
- [var learningRate: Float](mpsnnoptimizerdescriptor/learningrate.md)
- [var regularizationScale: Float](mpsnnoptimizerdescriptor/regularizationscale.md)
- [var regularizationType: MPSNNRegularizationType](mpsnnoptimizerdescriptor/regularizationtype.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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