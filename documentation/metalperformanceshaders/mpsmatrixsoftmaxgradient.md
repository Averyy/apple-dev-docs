# MPSMatrixSoftMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSMatrixSoftMaxGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixsoftmaxgradient/init(coder:device:).md)
- [init(device: any MTLDevice)](mpsmatrixsoftmaxgradient/init(device:).md)
### Instance Properties
- [var sourceColumns: Int](mpsmatrixsoftmaxgradient/sourcecolumns.md)
- [var sourceRows: Int](mpsmatrixsoftmaxgradient/sourcerows.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsmatrixsoftmaxgradient/copy(with:device:).md)
- [func encode(to: any MTLCommandBuffer, gradientMatrix: MPSMatrix, forwardOutputMatrix: MPSMatrix, resultMatrix: MPSMatrix)](mpsmatrixsoftmaxgradient/encode(to:gradientmatrix:forwardoutputmatrix:resultmatrix:).md)

## Relationships

### Inherits From
- [MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
### Inherited By
- [MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
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

- [class MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMax](mpsmatrixsoftmax.md)
  A softmax kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixsoftmaxgradient)*