# rowBytes

**Framework**: Metal Performance Shaders  
**Kind**: instp

The stride, in bytes, between corresponding elements of consecutive rows in the matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rowBytes: Int { get set }
```

#### Discussion

This value must be a multiple of the element size.

## See Also

- [var rows: Int](mpsmatrixdescriptor/2143203-rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrixdescriptor/2143196-columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrixdescriptor/2143202-datatype.md)
  The type of the values in the matrix.
- [enum MPSDataType](mpsdatatype.md)
  A value to specify a type of data.
- [var matrices: Int](mpsmatrixdescriptor/2873351-matrices.md)
- [var matrixBytes: Int](mpsmatrixdescriptor/2873387-matrixbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143199-rowbytes)*