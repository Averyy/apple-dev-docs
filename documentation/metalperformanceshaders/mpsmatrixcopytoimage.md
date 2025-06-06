# MPSMatrixCopyToImage

**Framework**: Metal Performance Shaders  
**Kind**: cl

A kernel that copies matrix data to a Metal Performance Shaders image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MPSMatrixCopyToImage : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsmatrixcopytoimage/2976459-init.md)
- [init(device: any MTLDevice, dataLayout: MPSDataLayout)](mpsmatrixcopytoimage/2976460-init.md)
### Instance Properties
- [var dataLayout: MPSDataLayout](mpsmatrixcopytoimage/2976457-datalayout.md)
- [var sourceMatrixBatchIndex: Int](mpsmatrixcopytoimage/2976461-sourcematrixbatchindex.md)
- [var sourceMatrixOrigin: MTLOrigin](mpsmatrixcopytoimage/2976462-sourcematrixorigin.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImage: MPSImage)](mpsmatrixcopytoimage/2976458-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceMatrix: MPSMatrix, destinationImages: [MPSImage])](mpsmatrixcopytoimage/3013770-encodebatch.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations. 
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixcopytoimage)*