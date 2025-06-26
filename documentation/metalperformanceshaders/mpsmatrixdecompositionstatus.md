# MPSMatrixDecompositionStatus

**Framework**: Metal Performance Shaders  
**Kind**: enum

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MPSMatrixDecompositionStatus
```

## Topics

### Enumeration Cases
- [MPSMatrixDecompositionStatus.failure](mpsmatrixdecompositionstatus/failure.md)
  A status indicating the decomposition was not able to be completed.
- [MPSMatrixDecompositionStatus.nonPositiveDefinite](mpsmatrixdecompositionstatus/nonpositivedefinite.md)
  A status indicating a non-positive-definite pivot value was calculated.
- [MPSMatrixDecompositionStatus.singular](mpsmatrixdecompositionstatus/singular.md)
  A status indicating the resulting decomposition is not suitable for use in a subsequent system solve.
- [MPSMatrixDecompositionStatus.success](mpsmatrixdecompositionstatus/success.md)
  A status indicating the decomposition was performed successfully.
### Initializers
- [init?(rawValue: Int32)](mpsmatrixdecompositionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MPSMatrixDecompositionCholesky](mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixSolveTriangular](mpsmatrixsolvetriangular.md)
  A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.
- [class MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdecompositionstatus)*