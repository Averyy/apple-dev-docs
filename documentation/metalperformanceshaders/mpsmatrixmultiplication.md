# MPSMatrixMultiplication

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSMatrixMultiplication
```

#### Overview

An [`MPSMatrixMultiplication`](mpsmatrixmultiplication.md) object computes the following operation:

Where , _,_ and  are matrices represented by [`MPSMatrix`](mpsmatrix.md) objects, and  and  are scalar values of the same data type as the values of .  and  may each have an optional transposition operation applied.

Matrices , , and  are also referred to as the left input matrix, the right input matrix, and the result matrix respectively.

## Topics

### Methods
- [init(device: any MTLDevice, transposeLeft: Bool, transposeRight: Bool, resultRows: Int, resultColumns: Int, interiorColumns: Int, alpha: Double, beta: Double)](mpsmatrixmultiplication/init(device:transposeleft:transposeright:resultrows:resultcolumns:interiorcolumns:alpha:beta:).md)
  Initializes a matrix multiplication kernel.
- [func encode(commandBuffer: any MTLCommandBuffer, leftMatrix: MPSMatrix, rightMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixmultiplication/encode(commandbuffer:leftmatrix:rightmatrix:resultmatrix:).md)
  Encodes a matrix multiplication kernel to a command buffer.
### Properties
- [var leftMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/leftmatrixorigin.md)
  The origin of the left input matrix.
- [var rightMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/rightmatrixorigin.md)
  The origin of the right input matrix.
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/resultmatrixorigin.md)
  The origin of the result matrix.
- [var batchSize: Int](mpsmatrixmultiplication/batchsize.md)
- [var batchStart: Int](mpsmatrixmultiplication/batchstart.md)
### Initializers
- [init(device: any MTLDevice, resultRows: Int, resultColumns: Int, interiorColumns: Int)](mpsmatrixmultiplication/init(device:resultrows:resultcolumns:interiorcolumns:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication)*