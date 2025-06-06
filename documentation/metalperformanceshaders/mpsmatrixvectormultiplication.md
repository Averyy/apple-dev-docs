# MPSMatrixVectorMultiplication

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSMatrixVectorMultiplication : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init(device: any MTLDevice, transpose: Bool, rows: Int, columns: Int, alpha: Double, beta: Double)](mpsmatrixvectormultiplication/2873083-init.md)
- [init(device: any MTLDevice, rows: Int, columns: Int)](mpsmatrixvectormultiplication/2909035-init.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, inputVector: MPSVector, resultVector: MPSVector)](mpsmatrixvectormultiplication/2873084-encode.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixvectormultiplication)*