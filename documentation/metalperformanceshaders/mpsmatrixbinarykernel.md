# MPSMatrixBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that consumes two matrices and produces one matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixBinaryKernel : MPSKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](mpsmatrixbinarykernel/2867089-batchsize.md)
- [var batchStart: Int](mpsmatrixbinarykernel/2867152-batchstart.md)
- [var primarySourceMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/2867182-primarysourcematrixorigin.md)
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/2867193-resultmatrixorigin.md)
- [var secondarySourceMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/2867096-secondarysourcematrixorigin.md)

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
- [class MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [enum MPSMatrixDecompositionStatus](mpsmatrixdecompositionstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixbinarykernel)*