# maximumPixelCount(forSpatialScaleFactor:)

**Framework**: Video Toolbox  
**Kind**: method

The maximum total number of pixels in the source frame for a given spatial scale factor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class func maximumPixelCount(forSpatialScaleFactor spatialScaleFactor: Int) -> Int
```

#### Discussion

The product of `frameWidth` and `frameHeight` must be less than or equal to this value. Use in conjunction with [`maximumDimension(forSpatialScaleFactor:)`](vtlowlatencyframeinterpolationconfiguration/maximumdimension(forspatialscalefactor:).md) to determine valid frame dimensions. Pass `1` for `spatialScaleFactor` when using the processor for temporal interpolation without spatial scaling. Returns `0` if an unsupported scale factor is provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtlowlatencyframeinterpolationconfiguration/maximumpixelcount(forspatialscalefactor:))*