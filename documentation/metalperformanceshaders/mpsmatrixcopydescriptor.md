# MPSMatrixCopyDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of multiple matrix copy operations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopyDescriptor
```

## Topics

### Initializers
- [init(device: any MTLDevice, count: Int)](mpsmatrixcopydescriptor/init(device:count:).md)
- [init(sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], offsetVector: MPSVector?, offset: Int)](mpsmatrixcopydescriptor/init(sourcematrices:destinationmatrices:offsetvector:offset:).md)
- [convenience init(sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](mpsmatrixcopydescriptor/init(sourcematrix:destinationmatrix:offsets:).md)
### Instance Methods
- [func setCopyOperationAt(Int, sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](mpsmatrixcopydescriptor/setcopyoperationat(_:sourcematrix:destinationmatrix:offsets:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations.
- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopydescriptor)*