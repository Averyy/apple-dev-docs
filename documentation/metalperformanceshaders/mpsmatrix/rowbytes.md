# rowBytes

**Framework**: Metal Performance Shaders  
**Kind**: property

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
var rowBytes: Int { get }
```

## See Also

- [var device: any MTLDevice](mpsmatrix/device.md)
  The device on which the matrix will be used.
- [var rows: Int](mpsmatrix/rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrix/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrix/datatype.md)
  The type of the values in the matrix.
- [var data: any MTLBuffer](mpsmatrix/data.md)
  The buffer that stores the matrix data.
- [var matrices: Int](mpsmatrix/matrices.md)
- [var matrixBytes: Int](mpsmatrix/matrixbytes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/rowbytes)*