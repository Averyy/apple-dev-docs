# MPSMatrixUnaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that consumes one matrix and produces one matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixUnaryKernel : MPSKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](mpsmatrixunarykernel/2867118-batchsize.md)
- [var batchStart: Int](mpsmatrixunarykernel/2866990-batchstart.md)
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixunarykernel/2867150-resultmatrixorigin.md)
- [var sourceMatrixOrigin: MTLOrigin](mpsmatrixunarykernel/2867053-sourcematrixorigin.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

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
- [class MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixunarykernel)*