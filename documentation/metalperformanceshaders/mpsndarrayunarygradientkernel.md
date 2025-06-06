# MPSNDArrayUnaryGradientKernel

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
class MPSNDArrayUnaryGradientKernel : MPSNDArrayMultiaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarrayunarygradientkernel/3175011-init.md)
- [init(device: any MTLDevice)](mpsndarrayunarygradientkernel/3143532-init.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarrayunarygradientkernel/3143530-encode.md)
- [func encode(to: any MTLCommandBuffer, sourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarrayunarygradientkernel/3143531-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarygradientkernel)*