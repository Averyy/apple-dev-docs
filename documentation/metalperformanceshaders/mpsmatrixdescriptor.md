# MPSMatrixDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

A description of attributes used to create an MPS matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixDescriptor : NSObject
```

#### Overview

Matrix data is assumed to be stored in row-major order.

## Topics

### Initializers
- [init(rows: Int, columns: Int, matrices: Int, rowBytes: Int, matrixBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/2873350-init.md)
- [init(rows: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/2873331-init.md)
### Methods
- [init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](mpsmatrixdescriptor/2143206-init.md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int](mpsmatrixdescriptor/2143204-rowbytes.md)
  Determines the recommended matrix row stride, in bytes, for a given number of columns.
- [class func rowBytes(forColumns: Int, dataType: MPSDataType) -> Int](mpsmatrixdescriptor/2873394-rowbytes.md)
### Properties
- [var rows: Int](mpsmatrixdescriptor/2143203-rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrixdescriptor/2143196-columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrixdescriptor/2143202-datatype.md)
  The type of the values in the matrix.
- [enum MPSDataType](mpsdatatype.md)
  A value to specify a type of data.
- [var rowBytes: Int](mpsmatrixdescriptor/2143199-rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var matrices: Int](mpsmatrixdescriptor/2873351-matrices.md)
- [var matrixBytes: Int](mpsmatrixdescriptor/2873387-matrixbytes.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSMatrix](mpsmatrix.md)
  A 2D array of data that stores the data's values.
- [class MPSTemporaryMatrix](mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor)*