# MPSNDArrayBinaryKernel

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
class MPSNDArrayBinaryKernel : MPSNDArrayMultiaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraybinarykernel/3175005-init.md)
- [init(device: any MTLDevice)](mpsndarraybinarykernel/3143501-init.md)
### Instance Properties
- [var primaryDilationRates: MPSNDArraySizes](mpsndarraybinarykernel/3143502-primarydilationrates.md)
- [var primaryEdgeMode: MPSImageEdgeMode](mpsndarraybinarykernel/3143503-primaryedgemode.md)
- [var primaryKernelSizes: MPSNDArraySizes](mpsndarraybinarykernel/3143504-primarykernelsizes.md)
- [var primaryOffsets: MPSNDArrayOffsets](mpsndarraybinarykernel/3143505-primaryoffsets.md)
- [var primaryStrides: MPSNDArrayOffsets](mpsndarraybinarykernel/3143506-primarystrides.md)
- [var secondaryDilationRates: MPSNDArraySizes](mpsndarraybinarykernel/3143507-secondarydilationrates.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsndarraybinarykernel/3143508-secondaryedgemode.md)
- [var secondaryKernelSizes: MPSNDArraySizes](mpsndarraybinarykernel/3143509-secondarykernelsizes.md)
- [var secondaryOffsets: MPSNDArrayOffsets](mpsndarraybinarykernel/3143510-secondaryoffsets.md)
- [var secondaryStrides: MPSNDArrayOffsets](mpsndarraybinarykernel/3143511-secondarystrides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray) -> MPSNDArray](mpsndarraybinarykernel/3143497-encode.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarraybinarykernel/3143498-encode.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarraybinarykernel/3143499-encode.md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarraybinarykernel/3143500-encode.md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarykernel)*