# MPSNDArrayBinaryKernel

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
class MPSNDArrayBinaryKernel
```

## Topics

### Initializers
- [init(coder: NSCoder, device: any MTLDevice)](mpsndarraybinarykernel/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsndarraybinarykernel/init(device:).md)
### Instance Properties
- [var primaryDilationRates: MPSNDArraySizes](mpsndarraybinarykernel/primarydilationrates.md)
- [var primaryEdgeMode: MPSImageEdgeMode](mpsndarraybinarykernel/primaryedgemode.md)
- [var primaryKernelSizes: MPSNDArraySizes](mpsndarraybinarykernel/primarykernelsizes.md)
- [var primaryOffsets: MPSNDArrayOffsets](mpsndarraybinarykernel/primaryoffsets.md)
- [var primaryStrides: MPSNDArrayOffsets](mpsndarraybinarykernel/primarystrides.md)
- [var secondaryDilationRates: MPSNDArraySizes](mpsndarraybinarykernel/secondarydilationrates.md)
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsndarraybinarykernel/secondaryedgemode.md)
- [var secondaryKernelSizes: MPSNDArraySizes](mpsndarraybinarykernel/secondarykernelsizes.md)
- [var secondaryOffsets: MPSNDArrayOffsets](mpsndarraybinarykernel/secondaryoffsets.md)
- [var secondaryStrides: MPSNDArrayOffsets](mpsndarraybinarykernel/secondarystrides.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray) -> MPSNDArray](mpsndarraybinarykernel/encode(to:primarysourcearray:secondarysourcearray:).md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, destinationArray: MPSNDArray)](mpsndarraybinarykernel/encode(to:primarysourcearray:secondarysourcearray:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: MPSState?, destinationArray: MPSNDArray)](mpsndarraybinarykernel/encode(to:primarysourcearray:secondarysourcearray:resultstate:destinationarray:).md)
- [func encode(to: any MTLCommandBuffer, primarySourceArray: MPSNDArray, secondarySourceArray: MPSNDArray, resultState: AutoreleasingUnsafeMutablePointer<MPSState?>?, outputStateIsTemporary: Bool) -> MPSNDArray](mpsndarraybinarykernel/encode(to:primarysourcearray:secondarysourcearray:resultstate:outputstateistemporary:).md)

## Relationships

### Inherits From
- [MPSNDArrayMultiaryKernel](mpsndarraymultiarykernel.md)
### Inherited By
- [MPSNDArrayGather](mpsndarraygather.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarykernel)*