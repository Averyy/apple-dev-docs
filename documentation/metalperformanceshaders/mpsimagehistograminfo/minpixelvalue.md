# minPixelValue

**Framework**: Metal Performance Shaders  
**Kind**: property

Specifies the minimum pixel value. Any pixel value less than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This minimum value is applied to each of the four channels separately.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var minPixelValue: vector_float4
```

## See Also

- [var numberOfHistogramEntries: Int](mpsimagehistograminfo/numberofhistogramentries.md)
  Specifies the number of histogram entries () for each channel.
- [var histogramForAlpha: ObjCBool](mpsimagehistograminfo/histogramforalpha.md)
  Specifies whether the histogram for the alpha channel should be computed or not.
- [var maxPixelValue: vector_float4](mpsimagehistograminfo/maxpixelvalue.md)
  Specifies the maximum pixel value.  Any pixel value greater than this will be clipped to this value (for the purposes of histogram calculation), and assigned to the first histogram entry. This maximum value is applied to each of the four channels separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo/minpixelvalue)*