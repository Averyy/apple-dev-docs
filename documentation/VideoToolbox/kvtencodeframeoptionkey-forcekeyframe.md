# kVTEncodeFrameOptionKey_ForceKeyFrame

**Framework**: Video Toolbox  
**Kind**: var

Boolean value indicating whether the current frame is forced to be a key frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTEncodeFrameOptionKey_ForceKeyFrame: CFString
```

#### Discussion

This value is set in the `frameProperties` dictionary passed to [`VTCompressionSessionEncodeFrame(_:imageBuffer:presentationTimeStamp:duration:frameProperties:sourceFrameRefcon:infoFlagsOut:)`](vtcompressionsessionencodeframe(_:imagebuffer:presentationtimestamp:duration:frameproperties:sourceframerefcon:infoflagsout:).md); it determines whether the current frame is forced to be a keyframe or not. Note that it may not be possible for the encoder to accommodate all requests.

## See Also

- [let kVTEncodeFrameOptionKey_BaseFrameQP: CFString](kvtencodeframeoptionkey_baseframeqp.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtencodeframeoptionkey_forcekeyframe)*