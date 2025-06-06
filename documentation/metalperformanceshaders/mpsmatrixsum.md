# MPSMatrixSum

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel for performing a pointwise summation of a matrix.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSum : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsum/2935614-init.md)
- [init(device: any MTLDevice, count: Int, rows: Int, columns: Int, transpose: Bool)](mpsmatrixsum/2935623-init.md)
### Instance Properties
- [var columns: Int](mpsmatrixsum/2935615-columns.md)
- [var count: Int](mpsmatrixsum/2935620-count.md)
- [var neuronParameterA: Float](mpsmatrixsum/2935624-neuronparametera.md)
- [var neuronParameterB: Float](mpsmatrixsum/2935616-neuronparameterb.md)
- [var neuronParameterC: Float](mpsmatrixsum/2935618-neuronparameterc.md)
- [var resultMatrixOrigin: MTLOrigin](mpsmatrixsum/3152564-resultmatrixorigin.md)
- [var rows: Int](mpsmatrixsum/2935622-rows.md)
- [var transpose: Bool](mpsmatrixsum/2935621-transpose.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceMatrices: [MPSMatrix], resultMatrix: MPSMatrix, scale: MPSVector?, offsetVector: MPSVector?, biasVector: MPSVector?, start: Int)](mpsmatrixsum/2935613-encode.md)
- [func neuronType() -> MPSCNNNeuronType](mpsmatrixsum/2935625-neurontype.md)
- [func setNeuronType(MPSCNNNeuronType, parameterA: Float, parameterB: Float, parameterC: Float)](mpsmatrixsum/2935617-setneurontype.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsum)*