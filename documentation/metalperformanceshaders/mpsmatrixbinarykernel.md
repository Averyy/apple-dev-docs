# MPSMatrixBinaryKernel

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSMatrixBinaryKernel
```

## Topics

### Instance Properties
- [var batchSize: Int](mpsmatrixbinarykernel/batchsize.md)
- [var batchStart: Int](mpsmatrixbinarykernel/batchstart.md)
- [var primarySourceMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/primarysourcematrixorigin.md)
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/resultmatrixorigin.md)
- [var secondarySourceMatrixOrigin: MTLOrigin](mpsmatrixbinarykernel/secondarysourcematrixorigin.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Inherited By
- [MPSMatrixBatchNormalizationGradient](mpsmatrixbatchnormalizationgradient.md)
- [MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
- [MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
- [MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
- [MPSMatrixSoftMaxGradient](mpsmatrixsoftmaxgradient.md)
- [MPSMatrixSolveCholesky](mpsmatrixsolvecholesky.md)
- [MPSMatrixSolveLU](mpsmatrixsolvelu.md)
- [MPSMatrixSolveTriangular](mpsmatrixsolvetriangular.md)
- [MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
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