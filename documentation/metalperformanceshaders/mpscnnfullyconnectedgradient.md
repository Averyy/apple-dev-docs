# MPSCNNFullyConnectedGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient fully connected convolution layer.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNFullyConnectedGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnfullyconnectedgradient/init(coder:device:).md)
- [init(device: any MTLDevice, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnectedgradient/init(device:weights:).md)

## Relationships

### Inherits From
- [MPSCNNConvolutionGradient](mpscnnconvolutiongradient.md)
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

- [class MPSCNNBinaryFullyConnected](mpscnnbinaryfullyconnected.md)
  A fully connected convolution layer with binary weights and optionally binarized input image.
- [class MPSCNNFullyConnected](mpscnnfullyconnected.md)
  A fully connected convolution layer, also known as an inner product layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectedgradient)*