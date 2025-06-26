# MPSImageAreaMin

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageAreaMin
```

#### Overview

An [`MPSImageAreaMin`](mpsimageareamin.md) filter has the same methods and properties as the [`MPSImageAreaMax`](mpsimageareamax.md) class.

If there are multiple channels in the source image, each channel is processed independently. The [`edgeMode`](mpsunaryimagekernel/edgemode.md) property value is assumed to always be [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) for this filter.

## Relationships

### Inherits From
- [MPSImageAreaMax](mpsimageareamax.md)
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

- [class MPSImageAreaMax](mpsimageareamax.md)
  A filter that finds the maximum pixel value in a rectangular region centered around each pixel in the source image.
- [class MPSImageDilate](mpsimagedilate.md)
  A filter that finds the maximum pixel value in a rectangular region by applying a dilation function.
- [class MPSImageErode](mpsimageerode.md)
  A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamin)*