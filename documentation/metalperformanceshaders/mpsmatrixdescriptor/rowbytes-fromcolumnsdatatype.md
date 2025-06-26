# rowBytes(fromColumns:dataType:)

**Framework**: Metal Performance Shaders  
**Kind**: method

Determines the recommended matrix row stride, in bytes, for a given number of columns.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func rowBytes(fromColumns columns: Int, dataType: MPSDataType) -> Int
```

#### Return Value

The recommended matrix row stride, in bytes.

#### Discussion

The optimal stride between the rows of a matrix is not necessarily equivalent to the number of columns in the matrix. This method returns the row stride, in bytes, which gives the best performance for a given number of columns. Using this row stride to construct your matrix descriptor is recommended, but not required (as long as the stride used is still large enough to allocate a full row of data).

## Parameters

- `columns`: The number of columns in the matrix.
- `dataType`: The type of the data to be stored in the matrix.

## See Also

- [convenience init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/init(dimensions:columns:rowbytes:datatype:).md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(forColumns: Int, dataType: MPSDataType) -> Int](mpsmatrixdescriptor/rowbytes(forcolumns:datatype:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/rowbytes(fromcolumns:datatype:))*