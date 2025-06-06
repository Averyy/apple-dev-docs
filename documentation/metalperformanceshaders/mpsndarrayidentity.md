# MPSNDArrayIdentity

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MPSNDArrayIdentity : MPSNDArrayUnaryKernel
```

## Topics

### Initializers
- [init(device: any MTLDevice)](mpsndarrayidentity/4438555-init.md)
### Instance Methods
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/4438558-reshape.md)
- [func reshape(with: (any MTLComputeCommandEncoder)?, commandBuffer: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/4438559-reshape.md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/4438556-reshape.md)
- [func reshape(with: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, shape: [NSNumber], destinationArray: MPSNDArray?) -> MPSNDArray?](mpsndarrayidentity/4438557-reshape.md)

## Relationships

### Inherits From
- [MPSNDArrayUnaryKernel](mpsndarrayunarykernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity)*