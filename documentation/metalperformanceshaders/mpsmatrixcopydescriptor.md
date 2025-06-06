# MPSMatrixCopyDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: cl

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
class MPSMatrixCopyDescriptor : NSObject
```

## Topics

### Initializers
- [init(device: any MTLDevice, count: Int)](mpsmatrixcopydescriptor/2915324-init.md)
- [init(sourceMatrices: [MPSMatrix], destinationMatrices: [MPSMatrix], offsetVector: MPSVector?, offset: Int)](mpsmatrixcopydescriptor/2915344-init.md)
- [init(sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](mpsmatrixcopydescriptor/2915333-init.md)
### Instance Methods
- [func setCopyOperationAt(Int, sourceMatrix: MPSMatrix, destinationMatrix: MPSMatrix, offsets: MPSMatrixCopyOffsets)](mpsmatrixcopydescriptor/2915331-setcopyoperationat.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations. 
- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopydescriptor)*