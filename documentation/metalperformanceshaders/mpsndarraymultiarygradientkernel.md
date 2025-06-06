# MPSNDArrayMultiaryGradientKernel

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
class MPSNDArrayMultiaryGradientKernel : MPSNDArrayMultiaryBase
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraymultiarygradientkernel/3175008-init.md)
- [init(device: any MTLDevice, sourceCount: Int, sourceGradientIndex: Int)](mpsndarraymultiarygradientkernel/3143524-init.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarraymultiarygradientkernel/3143522-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArrays: [MPSNDArray], sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarraymultiarygradientkernel/3143523-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryBase](mpsndarraymultiarybase.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarygradientkernel)*