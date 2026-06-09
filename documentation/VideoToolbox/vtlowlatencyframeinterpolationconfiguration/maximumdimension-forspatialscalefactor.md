# maximumDimension(forSpatialScaleFactor:)

**Framework**: Video Toolbox  
**Kind**: method

The maximum value for either dimension of the source frame, in pixels, for a given spatial scale factor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class func maximumDimension(forSpatialScaleFactor spatialScaleFactor: Int) -> Int
```

#### Discussion

Both `frameWidth` and `frameHeight` must be less than or equal to this value. Use in conjunction with [`maximumPixelCount(forSpatialScaleFactor:)`](vtlowlatencyframeinterpolationconfiguration/maximumpixelcount(forspatialscalefactor:).md) to determine valid frame dimensions. For example, if [`maximumDimension(forSpatialScaleFactor:)`](vtlowlatencyframeinterpolationconfiguration/maximumdimension(forspatialscalefactor:).md) is 1920 and [`maximumPixelCount(forSpatialScaleFactor:)`](vtlowlatencyframeinterpolationconfiguration/maximumpixelcount(forspatialscalefactor:).md) corresponds to 1920×1080, then 1920×1080, 1080×1920, and 1440×1440 are all valid, but 1920×1920 is not. Pass `1` for `spatialScaleFactor` when using the processor for temporal interpolation without spatial scaling. Returns `0` if an unsupported scale factor is provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/maximumdimension(forspatialscalefactor:))*