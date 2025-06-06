# MPSImageCopyToMatrix

**Framework**: Metal Performance Shaders  
**Kind**: cl

A class that copies image data to a matrix. 

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageCopyToMatrix : MPSKernel
```

#### Overview

This kernel copies image data to a [`MPSMatrix`](mpsmatrix.md) object. The image data is stored in a row of a matrix.  The [`dataLayout`](mpsimagecopytomatrix/2873216-datalayout.md) specifies the order in which the feature channels in the image get stored in the matrix.  If the [`MPSImage`](mpsimage.md) stores a batch of images, the images are copied into multiple rows, one row per image.

The number of elements in a row in the matrix must be greater than the image width multiplied its height multiplied by the number of [`featureChannels`](mpsimage/1648901-featurechannels.md) in the image.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagecopytomatrix/2873213-init.md)
- [init(device: any MTLDevice, dataLayout: MPSDataLayout)](mpsimagecopytomatrix/2873210-init.md)
### Instance Properties
- [var dataLayout: MPSDataLayout](mpsimagecopytomatrix/2873216-datalayout.md)
- [var destinationMatrixBatchIndex: Int](mpsimagecopytomatrix/2873211-destinationmatrixbatchindex.md)
- [var destinationMatrixOrigin: MTLOrigin](mpsimagecopytomatrix/2873215-destinationmatrixorigin.md)
### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer, sourceImage: MPSImage, destinationMatrix: MPSMatrix)](mpsimagecopytomatrix/2873212-encode.md)
- [func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], destinationMatrix: MPSMatrix)](mpsimagecopytomatrix/3013769-encodebatch.md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)

## See Also

- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations. 
- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecopytomatrix)*