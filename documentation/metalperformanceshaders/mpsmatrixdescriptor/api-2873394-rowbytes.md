# rowBytes(forColumns:dataType:)

**Framework**: Metal Performance Shaders  
**Kind**: clm

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func rowBytes(forColumns columns: Int, dataType: MPSDataType) -> Int
```

## See Also

- [init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/2143206-init.md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int](mpsmatrixdescriptor/2143204-rowbytes.md)
  Determines the recommended matrix row stride, in bytes, for a given number of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2873394-rowbytes)*