# kVTCompressionPropertyKey_ConstantQualityFactor

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let kVTCompressionPropertyKey_ConstantQualityFactor: CFString
```

#### Discussion

Requires the encoder to maintain consistent quality by specifying a target constant quality factor in the range of 0.0 to 1.0.

In contrast to cases where kVTCompressionPropertyKey_Quality will cause the quantization parameter to adhere to a fixed value, this property is designed for consistent visual quality with or without bitrate limit constraints. 0.0 is the lowest quality and 1.0 implies the highest quality possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_constantqualityfactor)*