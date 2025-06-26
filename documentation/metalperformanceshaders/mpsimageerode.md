# MPSImageErode

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that finds the minimum pixel value in a rectangular region by applying an erosion function.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageErode
```

#### Overview

An [`MPSImageErode`](mpsimageerode.md) behaves like the [`MPSImageAreaMin`](mpsimageareamin.md) filter, except that Metal calculates the intensity at each position relative to a different value before determining which is the maximum pixel value, allowing for shaped, nonrectangular morphological probes.

The code example below shows pseudocode for the calculation that returns each pixel value:

```other
for each pixel in the filter window
    value =  pixel[filterY][filterX] + filter[filterY*filter_width+filterX]
    if( value < bestValue ){
        result = value
        bestValue = value
    }
```

The definition of the [`MPSImageErode`](mpsimageerode.md) filter is different from its `vImage` counterpart (`MPSImageErode_filter_value = 1.0f-vImageErode_filter_value.`). This allows [`MPSImageDilate`](mpsimagedilate.md) and [`MPSImageErode`](mpsimageerode.md) to use the same filter, making open and close operators easier to write.

A filter that contains all zeros is identical to an [`MPSImageAreaMin`](mpsimageareamin.md) filter. Metal handles the center filter element as `0` to avoid causing a general lightening of the image, and it handles the [`edgeMode`](mpsunaryimagekernel/edgemode.md) property as [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) for this filter.

## Relationships

### Inherits From
- [MPSImageDilate](mpsimagedilate.md)
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
- [class MPSImageAreaMin](mpsimageareamin.md)
  A filter that finds the minimum pixel value in a rectangular region centered around each pixel in the source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageerode)*