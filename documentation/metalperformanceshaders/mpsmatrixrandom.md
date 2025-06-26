# MPSMatrixRandom

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixRandom
```

## Topics

### Instance Properties
- [var batchSize: Int](mpsmatrixrandom/batchsize.md)
- [var batchStart: Int](mpsmatrixrandom/batchstart.md)
- [var destinationDataType: MPSDataType](mpsmatrixrandom/destinationdatatype.md)
- [var distributionType: MPSMatrixRandomDistribution](mpsmatrixrandom/distributiontype.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, destinationMatrix: MPSMatrix)](mpsmatrixrandom/encode(commandbuffer:destinationmatrix:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, destinationVector: MPSVector)](mpsmatrixrandom/encode(commandbuffer:destinationvector:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSMatrixRandomMTGP32](mpsmatrixrandommtgp32.md)
- [MPSMatrixRandomPhilox](mpsmatrixrandomphilox.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandom)*