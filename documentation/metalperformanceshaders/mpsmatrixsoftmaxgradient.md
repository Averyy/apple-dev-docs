# MPSMatrixSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: cl

A gradient softmax kernel that operates on matrices.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSoftMaxGradient : MPSMatrixBinaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsoftmaxgradient/2966653-init.md)
- [init(device: any MTLDevice)](mpsmatrixsoftmaxgradient/2966654-init.md)
### Instance Properties
- [var sourceColumns: Int](mpsmatrixsoftmaxgradient/2966655-sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixsoftmaxgradient/2966656-sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixsoftmaxgradient/2966651-copy.md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, forwardOutputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixsoftmaxgradient/2966652-encode.md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)

## See Also

- [class MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMax](mpsmatrixsoftmax.md)
  A softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmaxgradient)*