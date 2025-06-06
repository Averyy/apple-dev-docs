# MPSMatrixCopy

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that can perform multiple matrix copy operations. 

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopy : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixcopy/2915334-init.md)
- [init(device: any MTLDevice, copyRows: Int, copyColumns: Int, sourcesAreTransposed: Bool, destinationsAreTransposed: Bool)](mpsmatrixcopy/2915345-init.md)
### Instance Properties
- [var copyColumns: Int](mpsmatrixcopy/2915325-copycolumns.md)
- [var copyRows: Int](mpsmatrixcopy/2915342-copyrows.md)
- [var destinationsAreTransposed: Bool](mpsmatrixcopy/2915326-destinationsaretransposed.md)
- [var sourcesAreTransposed: Bool](mpsmatrixcopy/2915340-sourcesaretransposed.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor)](mpsmatrixcopy/2915341-encode.md)
- [func encode(commandBuffer: any MTLCommandBuffer, copyDescriptor: MPSMatrixCopyDescriptor, rowPermuteIndices: MPSVector?, rowPermuteOffset: Int, columnPermuteIndices: MPSVector?, columnPermuteOffset: Int)](mpsmatrixcopy/2935558-encode.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopy)*