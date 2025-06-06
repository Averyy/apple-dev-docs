# MPSTemporaryVector

**Framework**: Metal Performance Shaders  
**Kind**: cl

A vector allocated on GPU private memory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSTemporaryVector : MPSVector
```

## Topics

### Initializers
- [init(commandBuffer: any MTLCommandBuffer, descriptor: MPSVectorDescriptor)](mpstemporaryvector/2935550-init.md)
### Instance Properties
- [var readCount: Int](mpstemporaryvector/2935547-readcount.md)
### Type Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, descriptorList: [MPSVectorDescriptor])](mpstemporaryvector/2935544-prefetchstorage.md)

## Relationships

### Inherits From
- [MPSVector](mpsvector.md)

## See Also

- [class MPSVector](mpsvector.md)
  A 1D array of data that stores the data's values.
- [class MPSVectorDescriptor](mpsvectordescriptor.md)
  A description of the length and data type of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryvector)*