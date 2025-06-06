# MPSCommandBuffer

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
class MPSCommandBuffer : NSObject
```

## Topics

### Initializers
- [init(commandBuffer: any MTLCommandBuffer)](mpscommandbuffer/3114031-init.md)
- [init(from: any MTLCommandQueue)](mpscommandbuffer/3114029-init.md)
### Instance Properties
- [var commandBuffer: any MTLCommandBuffer](mpscommandbuffer/3114028-commandbuffer.md)
- [var heapProvider: (any MPSHeapProvider)?](mpscommandbuffer/3229857-heapprovider.md)
- [var predicate: MPSPredicate?](mpscommandbuffer/3114032-predicate.md)
- [var rootCommandBuffer: any MTLCommandBuffer](mpscommandbuffer/3166772-rootcommandbuffer.md)
### Instance Methods
- [func commitAndContinue()](mpscommandbuffer/3152524-commitandcontinue.md)
- [func prefetchHeap(forWorkloadSize: Int)](mpscommandbuffer/3229858-prefetchheap.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [MTLCommandBuffer](../metal/mtlcommandbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscommandbuffer)*