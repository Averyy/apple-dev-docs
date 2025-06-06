# MPSVector

**Framework**: Metal Performance Shaders  
**Kind**: cl

A 1D array of data that stores the data's values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSVector : NSObject
```

## Topics

### Initializers
- [init(buffer: any MTLBuffer, descriptor: MPSVectorDescriptor)](mpsvector/2873346-init.md)
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSVectorDescriptor)](mpsvector/3229864-init.md)
- [init(device: any MTLDevice, descriptor: MPSVectorDescriptor)](mpsvector/2942566-init.md)
### Instance Properties
- [var data: any MTLBuffer](mpsvector/2873393-data.md)
- [var dataType: MPSDataType](mpsvector/2873336-datatype.md)
- [var device: any MTLDevice](mpsvector/2873338-device.md)
- [var length: Int](mpsvector/2873392-length.md)
- [var vectorBytes: Int](mpsvector/2873340-vectorbytes.md)
- [var vectors: Int](mpsvector/2873388-vectors.md)
- [var offset: Int](mpsvector/3375741-offset.md)
### Instance Methods
- [func resourceSize() -> Int](mpsvector/2942570-resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsvector/2942568-synchronize.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSVectorDescriptor](mpsvectordescriptor.md)
  A description of the length and data type of a vector.
- [class MPSTemporaryVector](mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvector)*