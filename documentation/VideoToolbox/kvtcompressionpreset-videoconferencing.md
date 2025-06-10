# kVTCompressionPreset_VideoConferencing

**Framework**: Video Toolbox  
**Kind**: var

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let kVTCompressionPreset_VideoConferencing: CFString
```

#### Discussion

```None
A preset to achieve low-latency encoding for real-time communication applications.
```

This preset requires setting kVTVideoEncoderSpecification_EnableLowLatencyRateControl to kCFBooleanTrue for encoding in the low-latency mode.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_videoconferencing)*