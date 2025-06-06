# MPSNDArrayMultiaryKernel

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
class MPSNDArrayMultiaryKernel : MPSNDArrayMultiaryBase
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarykernel/3175009-init.md)
- [init(device: any MTLDevice, sourceCount: Int)](mpsndarraymultiarykernel/3175010-init.md)
### Instance Methods
- [func encode(to: (any MTLComputeCommandEncoder)?, commandBuffer: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](mpsndarraymultiarykernel/4462738-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray]) -> MPSNDArray](mpsndarraymultiarykernel/3143525-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray: MPSNDArray)](mpsndarraymultiarykernel/3143526-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarraymultiarykernel/3143527-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarraymultiarykernel/3143528-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](mpsndarraymultiarybase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel)*