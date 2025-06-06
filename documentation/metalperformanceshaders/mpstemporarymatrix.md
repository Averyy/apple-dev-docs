# MPSTemporaryMatrix

**Framework**: Metal Performance Shaders  
**Kind**: cl

A matrix allocated on GPU private memory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSTemporaryMatrix : MPSMatrix
```

## Topics

### Initializers
- [init(commandBuffer: any MTLCommandBuffer, matrixDescriptor: MPSMatrixDescriptor)](mpstemporarymatrix/2867180-init.md)
### Instance Properties
- [var readCount: Int](mpstemporarymatrix/2867151-readcount.md)
### Type Methods
- [class func prefetchStorage(with: any MTLCommandBuffer, matrixDescriptorList: [MPSMatrixDescriptor])](mpstemporarymatrix/2867073-prefetchstorage.md)

## Relationships

### Inherits From
- [MPSMatrix](mpsmatrix.md)

## See Also

- [class MPSMatrix](mpsmatrix.md)
  A 2D array of data that stores the data's values.
- [class MPSMatrixDescriptor](mpsmatrixdescriptor.md)
  A description of attributes used to create an MPS matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporarymatrix)*