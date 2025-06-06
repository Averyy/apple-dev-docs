# MPSMatrixFindTopK

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel for computing the top-K values and their corresponding indices in a matrix.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixFindTopK : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixfindtopk/2935582-init.md)
- [init(device: any MTLDevice, numberOfTopKValues: Int)](mpsmatrixfindtopk/2935575-init.md)
### Instance Properties
- [var indexOffset: Int](mpsmatrixfindtopk/2935574-indexoffset.md)
- [var numberOfTopKValues: Int](mpsmatrixfindtopk/2935577-numberoftopkvalues.md)
- [var sourceColumns: Int](mpsmatrixfindtopk/2935573-sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixfindtopk/2935580-sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixfindtopk/2935581-copy.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultIndexMatrix: MPSMatrix, resultValueMatrix: MPSMatrix)](mpsmatrixfindtopk/2935579-encode.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)

## See Also

- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixfindtopk)*