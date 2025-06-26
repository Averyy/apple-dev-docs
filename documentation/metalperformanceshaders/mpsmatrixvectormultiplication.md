# MPSMatrixVectorMultiplication

**Framework**: Metal Performance Shaders  
**Kind**: class

A matrix-vector multiplication kernel

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixVectorMultiplication
```

## Topics

### Initializers
- [init(device: any MTLDevice, transpose: Bool, rows: Int, columns: Int, alpha: Double, beta: Double)](mpsmatrixvectormultiplication/init(device:transpose:rows:columns:alpha:beta:).md)
- [init(device: any MTLDevice, rows: Int, columns: Int)](mpsmatrixvectormultiplication/init(device:rows:columns:).md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, inputVector: MPSVector, resultVector: MPSVector)](mpsmatrixvectormultiplication/encode(commandbuffer:inputmatrix:inputvector:resultvector:).md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
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
- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixvectormultiplication)*