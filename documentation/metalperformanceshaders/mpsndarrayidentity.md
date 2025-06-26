# MPSNDArrayIdentity

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MPSNDArrayIdentity
```

## Topics

### Initializers
- [init(device: any MTLDevice)](mpsndarrayidentity/init(device:).md)
### Instance Methods
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/reshape(with:commandbuffer:sourcearray:dimensioncount:dimensionsizes:destinationarray:).md)
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/reshape(with:commandbuffer:sourcearray:shape:destinationarray:).md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/reshape(with:sourcearray:dimensioncount:dimensionsizes:destinationarray:).md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/reshape(with:sourcearray:shape:destinationarray:).md)

## Relationships

### Inherits From
- [MPSNDArrayUnaryKernel](mpsndarrayunarykernel.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity)*