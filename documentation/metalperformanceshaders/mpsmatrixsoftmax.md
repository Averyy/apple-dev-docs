# MPSMatrixSoftMax

**Framework**: Metal Performance Shaders  
**Kind**: cl

A softmax kernel that operates on matrices.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixSoftMax : MPSMatrixUnaryKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsoftmax/2935565-init.md)
- [init(device: any MTLDevice)](mpsmatrixsoftmax/2935562-init.md)
### Instance Properties
- [var sourceColumns: Int](mpsmatrixsoftmax/2935560-sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixsoftmax/2935561-sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixsoftmax/2935566-copy.md)
- [func encode(commandBuffer: any MTLCommandBuffer, inputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixsoftmax/2935563-encode.md)

## Relationships

### Inherits From
- [MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)

## See Also

- [class MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMaxGradient](mpsmatrixsoftmaxgradient.md)
  A gradient softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmax)*