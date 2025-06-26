# MPSCustomKernelArgumentCount

**Framework**: Metal Performance Shaders  
**Kind**: struct

A structure that contains the number of destination, source, and broadcaset textures used by a custom kernel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSCustomKernelArgumentCount
```

## Topics

### Initializers
- [init()](mpscustomkernelargumentcount/init.md)
- [init(destinationTextureCount: UInt, sourceTextureCount: UInt, broadcastTextureCount: UInt)](mpscustomkernelargumentcount/init(destinationtexturecount:sourcetexturecount:broadcasttexturecount:).md)
### Instance Properties
- [var broadcastTextureCount: UInt](mpscustomkernelargumentcount/broadcasttexturecount.md)
- [var destinationTextureCount: UInt](mpscustomkernelargumentcount/destinationtexturecount.md)
- [var sourceTextureCount: UInt](mpscustomkernelargumentcount/sourcetexturecount.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelargumentcount)*