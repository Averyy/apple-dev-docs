# MPSNDArrayUnaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNDArrayUnaryKernel : MPSNDArrayMultiaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarrayunarykernel/3175012-init.md)
- [init(device: any MTLDevice)](mpsndarrayunarykernel/3143540-init.md)
### Instance Properties
- [var dilationRates: MPSNDArraySizes](mpsndarrayunarykernel/3143534-dilationrates.md)
- [var edgeMode: MPSImageEdgeMode](mpsndarrayunarykernel/3143535-edgemode.md)
- [var kernelSizes: MPSNDArraySizes](mpsndarrayunarykernel/3143541-kernelsizes.md)
- [var offsets: MPSNDArrayOffsets](mpsndarrayunarykernel/3143542-offsets.md)
- [var strides: MPSNDArrayOffsets](mpsndarrayunarykernel/3143543-strides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray) -> MPSNDArray](mpsndarrayunarykernel/3143536-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarrayunarykernel/3143537-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarrayunarykernel/3143538-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarrayunarykernel/3143539-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel)*