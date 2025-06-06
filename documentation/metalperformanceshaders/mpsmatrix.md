# MPSMatrix

**Framework**: Metalperformanceshaders  
**Kind**: cl

A 2D array of data that stores the data's values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrix : NSObject
```

#### Overview

[`MPSMatrix`](mpsmatrix.md) objects serve as inputs and outputs of [`MPSMatrixMultiplication`](mpsmatrixmultiplication.md) objects. Matrix data is assumed to be stored in row-major order.

> **Note**: An [`MPSMatrix`](mpsmatrix.md) object maintains its internal storage using a [`MTLBuffer`](https://developer.apple.com/documentation/metal/mtlbuffer) object. Thus, the same rules for maintaining coherency of the buffer’s data between CPU memory and GPU memory also apply to an [`MPSMatrix`](mpsmatrix.md) object.

## Topics

### Methods
- [init(buffer: any MTLBuffer, descriptor: MPSMatrixDescriptor)](mpsmatrix/2143201-init.md)
  Initializes a matrix with a buffer.
### Properties
- [var device: any MTLDevice](mpsmatrix/2143209-device.md)
  The device on which the matrix will be used.
- [var rows: Int](mpsmatrix/2143210-rows.md)
  The number of rows in the matrix.
- [var columns: Int](mpsmatrix/2143207-columns.md)
  The number of columns in the matrix.
- [var dataType: MPSDataType](mpsmatrix/2143197-datatype.md)
  The type of the values in the matrix.
- [var rowBytes: Int](mpsmatrix/2143208-rowbytes.md)
  The stride, in bytes, between corresponding elements of consecutive rows in the matrix.
- [var data: any MTLBuffer](mpsmatrix/2143205-data.md)
  The buffer that stores the matrix data.
- [var matrices: Int](mpsmatrix/2873334-matrices.md)
- [var matrixBytes: Int](mpsmatrix/2873344-matrixbytes.md)
### Initializers
- [init(buffer: any MTLBuffer, offset: Int, descriptor: MPSMatrixDescriptor)](mpsmatrix/3229863-init.md)
- [init(device: any MTLDevice, descriptor: MPSMatrixDescriptor)](mpsmatrix/2942567-init.md)
### Instance Properties
- [var offset: Int](mpsmatrix/3375740-offset.md)
### Instance Methods
- [func resourceSize() -> Int](mpsmatrix/2942569-resourcesize.md)
- [func synchronize(on: any MTLCommandBuffer)](mpsmatrix/2942571-synchronize.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSMatrixDescriptor](mpsmatrixdescriptor.md)
  A description of attributes used to create an MPS matrix.
- [class MPSTemporaryMatrix](mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix)*