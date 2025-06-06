# numberOfHistogramEntries

**Framework**: Metal Performance Shaders  
**Kind**: structp

Specifies the number of histogram entries () for each channel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var numberOfHistogramEntries: Int
```

#### Discussion

This value must be both a power of 2 and a minimum of 256 bins.

For example, if you want 256 histogram bins then this value must be set to 256. The value stored in each histogram bin is a 32-bit unsigned integer. The size of the histogram buffer in which these bins will be stored should be more than or equal to:

`number of histogram entries * sizeof(uint32_t) * number of channels in the image`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo/1618805-numberofhistogramentries)*