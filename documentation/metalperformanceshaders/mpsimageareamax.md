# MPSImageAreaMax

**Framework**: Metal Performance Shaders  
**Kind**: cl

A filter that finds the maximum pixel value in a rectangular region centered around each pixel in the source image. 

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageAreaMax : MPSUnaryImageKernel
```

#### Overview

If there are multiple channels in the source image, each channel is processed independently. The [`edgeMode`](mpsunaryimagekernel/1618812-edgemode.md) property value is assumed to always be [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) for this filter.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageareamax/2866327-init.md)
### Methods
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpsimageareamax/1618281-init.md)
  Initializes the kernel with a specified width and height.
### Properties
- [var kernelHeight: Int](mpsimageareamax/1618277-kernelheight.md)
  The height of the filter window. Must be an odd number.
- [var kernelWidth: Int](mpsimageareamax/1618282-kernelwidth.md)
  The width of the filter window. Must be an odd number.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)

## See Also

- [class MPSImageDilate](mpsimagedilate.md)
  A filter that finds the maximum pixel value in a rectangular region by applying a dilation function. 
- [class MPSImageAreaMin](mpsimageareamin.md)
  A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image. 
- [class MPSImageErode](mpsimageerode.md)
  A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax)*