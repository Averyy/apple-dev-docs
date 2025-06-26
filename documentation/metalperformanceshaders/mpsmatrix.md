# MPSMatrix

**Framework**: Metal Performance Shaders  
**Kind**: class

A 2D array of data that stores the data’s values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrix
```

#### Overview

[`MPSMatrix`](mpsmatrix.md) objects serve as inputs and outputs of [`MPSMatrixMultiplication`](mpsmatrixmultiplication.md) objects. Matrix data is assumed to be stored in row-major order.

> **Note**:  An [`MPSMatrix`](mpsmatrix.md) object maintains its internal storage using a [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) object. Thus, the same rules for maintaining coherency of the buffer’s data between CPU memory and GPU memory also apply to an [`MPSMatrix`](mpsmatrix.md) object.

## Topics

### Methods
- [init(buffer: any MTLBuffer, descriptor: MPSMatrixDescriptor)](mpsmatrix/init(buffer:descriptor:).md)
  Initializes a matrix with a buffer.
### Properties
- [var device: any MTLDevice](mpsmatrix/device.md)
  The device on which the matrix will be used.
- [var rows: Int](mpsmatrix/rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrix/columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrix/datatype.md)
  The type of the values in the matrix.
- [var rowBytes: Int](mpsmatrix/rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var data: any MTLBuffer](mpsmatrix/data.md)
  The buffer that stores the matrix data.
- [var matrices: Int](mpsmatrix/matrices.md)
- [var matrixBytes: Int](mpsmatrix/matrixbytes.md)
### Initializers
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSMatrixDescriptor)](mpsmatrix/init(buffer:offset:descriptor:).md)
- [init(device: any MTLDevice, descriptor: MPSMatrixDescriptor)](mpsmatrix/init(device:descriptor:).md)
### Instance Properties
- [var offset: Int](mpsmatrix/offset.md)
### Instance Methods
- [func resourceSize() -> Int](mpsmatrix/resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsmatrix/synchronize(on:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPSTemporaryMatrix](mpstemporarymatrix.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSMatrixDescriptor](mpsmatrixdescriptor.md)
  A description of attributes used to create an MPS matrix.
- [class MPSTemporaryMatrix](mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix)*