# MPSVectorDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

A description of the length and data type of a vector.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSVectorDescriptor : NSObject
```

## Topics

### Initializers
- [init(length: Int, dataType: MPSDataType)](mpsvectordescriptor/2873328-init.md)
- [init(length: Int, vectors: Int, vectorBytes: Int, dataType: MPSDataType)](mpsvectordescriptor/2873348-init.md)
### Instance Properties
- [var dataType: MPSDataType](mpsvectordescriptor/2873362-datatype.md)
- [var length: Int](mpsvectordescriptor/2873345-length.md)
- [var vectorBytes: Int](mpsvectordescriptor/2873335-vectorbytes.md)
- [var vectors: Int](mpsvectordescriptor/2873333-vectors.md)
### Type Methods
- [class func vectorBytes(forLength: Int, dataType: MPSDataType) -> Int](mpsvectordescriptor/2873337-vectorbytes.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSVector](mpsvector.md)
  A 1D array of data that stores the data's values.
- [class MPSTemporaryVector](mpstemporaryvector.md)
  A vector allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsvectordescriptor)*