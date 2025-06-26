# MPSVector

**Framework**: Metal Performance Shaders  
**Kind**: class

A 1D array of data that stores the data’s values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSVector
```

## Topics

### Initializers
- [init(buffer: any MTLBuffer, descriptor: MPSVectorDescriptor)](mpsvector/init(buffer:descriptor:).md)
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSVectorDescriptor)](mpsvector/init(buffer:offset:descriptor:).md)
- [init(device: any MTLDevice, descriptor: MPSVectorDescriptor)](mpsvector/init(device:descriptor:).md)
### Instance Properties
- [var data: any MTLBuffer](mpsvector/data.md)
- [var dataType: MPSDataType](mpsvector/datatype.md)
- [var device: any MTLDevice](mpsvector/device.md)
- [var length: Int](mpsvector/length.md)
- [var vectorBytes: Int](mpsvector/vectorbytes.md)
- [var vectors: Int](mpsvector/vectors.md)
- [var offset: Int](mpsvector/offset.md)
### Instance Methods
- [func resourceSize() -> Int](mpsvector/resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsvector/synchronize(on:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSTemporaryVector](mpstemporaryvector.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSVectorDescriptor](mpsvectordescriptor.md)
  A description of the length and data type of a vector.
- [class MPSTemporaryVector](mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvector)*