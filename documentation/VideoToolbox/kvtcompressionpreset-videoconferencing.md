# kVTCompressionPreset_VideoConferencing

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
let kVTCompressionPreset_VideoConferencing: CFString
```

#### Discussion

A preset to achieve low-latency encoding for real-time communication applications.

This preset requires setting kVTVideoEncoderSpecification_EnableLowLatencyRateControl to kCFBooleanTrue for encoding in the low-latency mode.

```None
See also kVTCompressionPreset_HighQuality, kVTCompressionPreset_Balanced, kVTCompressionPreset_HighSpeed.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpreset_videoconferencing)*