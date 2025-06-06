# MPSMatrixMultiplication

**Framework**: Metal Performance Shaders  
**Kind**: cl

A matrix multiplication kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixMultiplication : MPSKernel
```

#### Overview

An [`MPSMatrixMultiplication`](mpsmatrixmultiplication.md) object computes the following operation:

Where ,  and  are matrices represented by [`MPSMatrix`](mpsmatrix.md) objects, and  and  are scalar values of the same data type as the values of .  and  may each have an optional transposition operation applied.

Matrices , , and  are also referred to as the left input matrix, the right input matrix, and the result matrix respectively.

## Topics

### Methods
- [init(device: any MTLDevice, transposeLeft: Bool, transposeRight: Bool, resultRows: Int, resultColumns: Int, interiorColumns: Int, alpha: Double, beta: Double)](mpsmatrixmultiplication/2147845-init.md)
  Initializes a matrix multiplication kernel.
- [func encode(commandBuffer: any MTLCommandBuffer, leftMatrix: MPSMatrix, rightMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixmultiplication/2147848-encode.md)
  Encodes a matrix multiplication kernel to a command buffer.
### Properties
- [var leftMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/2147846-leftmatrixorigin.md)
  The origin of the left input matrix.
- [var rightMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/2147851-rightmatrixorigin.md)
  The origin of the right input matrix.
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/2147847-resultmatrixorigin.md)
  The origin of the result matrix.
- [var batchSize: Int](mpsmatrixmultiplication/2873082-batchsize.md)
- [var batchStart: Int](mpsmatrixmultiplication/2873081-batchstart.md)
### Initializers
- [init(device: any MTLDevice, resultRows: Int, resultColumns: Int, interiorColumns: Int)](mpsmatrixmultiplication/2909034-init.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication)*