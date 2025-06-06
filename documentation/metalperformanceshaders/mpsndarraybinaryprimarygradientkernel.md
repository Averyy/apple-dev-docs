# MPSNDArrayBinaryPrimaryGradientKernel

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
class MPSNDArrayBinaryPrimaryGradientKernel : MPSNDArrayMultiaryGradientKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraybinaryprimarygradientkernel/3175006-init.md)
- [init(device: any MTLDevice)](mpsndarraybinaryprimarygradientkernel/3143515-init.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState) -> MPSNDArray](mpsndarraybinaryprimarygradientkernel/3143513-encode.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, sourceGradient: MPSNDArray, gradientState: MPSState, destinationArray: MPSNDArray)](mpsndarraybinaryprimarygradientkernel/3143514-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryGradientKernel](mpsndarraymultiarygradientkernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinaryprimarygradientkernel)*