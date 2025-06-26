# histogramForAlpha

**Framework**: Metal Performance Shaders  
**Kind**: property

Specifies whether the histogram for the alpha channel should be computed or not.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var histogramForAlpha: ObjCBool
```

## See Also

- [var numberOfHistogramEntries: Int](mpsimagehistograminfo/numberofhistogramentries.md)
  Specifies the number of histogram entries () for each channel.
- [var minPixelValue: vector_float4](mpsimagehistograminfo/minpixelvalue.md)
  Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.
- [var maxPixelValue: vector_float4](mpsimagehistograminfo/maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo/histogramforalpha)*