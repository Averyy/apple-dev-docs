# MPSCustomKernelInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSCustomKernelInfo
```

## Topics

### Initializers
- [init()](mpscustomkernelinfo/init.md)
- [init(clipOrigin: vector_ushort4, clipSize: vector_ushort4, destinationFeatureChannels: UInt16, destImageArraySize: UInt16, sourceImageCount: UInt16, threadgroupSize: UInt16, subbatchIndex: UInt16, subbatchStride: UInt16, idiv: MPSIntegerDivisionParams)](mpscustomkernelinfo/init(cliporigin:clipsize:destinationfeaturechannels:destimagearraysize:sourceimagecount:threadgroupsize:subbatchindex:subbatchstride:idiv:).md)
### Instance Properties
- [var clipOrigin: vector_ushort4](mpscustomkernelinfo/cliporigin.md)
- [var clipSize: vector_ushort4](mpscustomkernelinfo/clipsize.md)
- [var destImageArraySize: UInt16](mpscustomkernelinfo/destimagearraysize.md)
- [var destinationFeatureChannels: UInt16](mpscustomkernelinfo/destinationfeaturechannels.md)
- [var idiv: MPSIntegerDivisionParams](mpscustomkernelinfo/idiv.md)
- [var sourceImageCount: UInt16](mpscustomkernelinfo/sourceimagecount.md)
- [var subbatchIndex: UInt16](mpscustomkernelinfo/subbatchindex.md)
- [var subbatchStride: UInt16](mpscustomkernelinfo/subbatchstride.md)
- [var threadgroupSize: UInt16](mpscustomkernelinfo/threadgroupsize.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelinfo)*