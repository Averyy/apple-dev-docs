# kVTDecodeFrameOptionKey_ContentAnalyzerRotation

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let kVTDecodeFrameOptionKey_ContentAnalyzerRotation: CFString
```

#### Discussion

Clockwise rotation (one of 0, 90, 180, 270) to be applied for proper display orientation.

This value is used for content analysis to properly orient the image before analysis. The value should be a CFNumber with values of 0, 90, 180, or 270, representing degrees of clockwise rotation. This key is not used unless you have attached a `SCVideoStreamAnalyzer` to the decompression session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtdecodeframeoptionkey_contentanalyzerrotation)*