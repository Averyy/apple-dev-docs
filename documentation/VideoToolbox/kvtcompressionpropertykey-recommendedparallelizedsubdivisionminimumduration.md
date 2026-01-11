# kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration

**Framework**: Video Toolbox  
**Kind**: var

The recommended minimum duration for a given subdivision in a parallel encoding configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumDuration: CFString
```

#### Discussion

For best results, ensure that the total duration of a parallelized subdivision is greater than or equal to this value.

> **Note**:  This configuration isn’t supported by all video encoders.

## See Also

- [let kVTCompressionPropertyKey_RecommendedParallelizationLimit: CFString](kvtcompressionpropertykey_recommendedparallelizationlimit.md)
  The recommended number of compression sessions to instantiate in a parallel encoding configuration.
- [let kVTCompressionPropertyKey_RecommendedParallelizedSubdivisionMinimumFrameCount: CFString](kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumframecount.md)
  The recommended minimum number of video frames for a given subdivision in a parallel encoding configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_recommendedparallelizedsubdivisionminimumduration)*