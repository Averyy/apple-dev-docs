# rowBytes(fromColumns:dataType:)

**Framework**: Metal Performance Shaders  
**Kind**: clm

Determines the recommended matrix row stride, in bytes, for a given number of columns.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- macOS 10.13+
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func rowBytes(fromColumns columns: Int, dataType: MPSDataType) -> Int
```

#### Return_value

The recommended matrix row stride, in bytes.

#### Discussion

The optimal stride between the rows of a matrix is not necessarily equivalent to the number of columns in the matrix. This method returns the row stride, in bytes, which gives the best performance for a given number of columns. Using this row stride to construct your matrix descriptor is recommended, but not required (as long as the stride used is still large enough to allocate a full row of data).

## Parameters

- `columns`: The number of columns in the matrix.
- `dataType`: The type of the data to be stored in the matrix.

## See Also

- [init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/2143206-init.md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(forColumns: Int, dataType: MPSDataType) -> Int](mpsmatrixdescriptor/2873394-rowbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143204-rowbytes)*