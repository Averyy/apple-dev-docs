# MPSImageAreaMax

**Framework**: Metal Performance Shaders  
**Kind**: class

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
class MPSImageAreaMax
```

#### Overview

If there are multiple channels in the source image, each channel is processed independently. The [`edgeMode`](mpsunaryimagekernel/edgemode.md) property value is assumed to always be [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) for this filter.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageareamax/init(coder:device:).md)
### Methods
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpsimageareamax/init(device:kernelwidth:kernelheight:).md)
  Initializes the kernel with a specified width and height.
### Properties
- [var kernelHeight: Int](mpsimageareamax/kernelheight.md)
  The height of the filter window. Must be an odd number.
- [var kernelWidth: Int](mpsimageareamax/kernelwidth.md)
  The width of the filter window. Must be an odd number.

## Relationships

### Inherits From
- [MPSUnaryImageKernel](mpsunaryimagekernel.md)
### Inherited By
- [MPSImageAreaMin](mpsimageareamin.md)
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

- [class MPSImageDilate](mpsimagedilate.md)
  A filter that finds the maximum pixel value in a rectangular region by applying a dilation function.
- [class MPSImageAreaMin](mpsimageareamin.md)
  A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image.
- [class MPSImageErode](mpsimageerode.md)
  A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax)*