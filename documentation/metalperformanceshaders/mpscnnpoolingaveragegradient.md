# MPSCNNPoolingAverageGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient average pooling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingAverageGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpoolingaveragegradient/init(coder:device:).md)
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolingaveragegradient/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
### Instance Properties
- [var zeroPadSizeX: Int](mpscnnpoolingaveragegradient/zeropadsizex.md)
- [var zeroPadSizeY: Int](mpscnnpoolingaveragegradient/zeropadsizey.md)

## Relationships

### Inherits From
- [MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
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

- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingaveragegradient)*