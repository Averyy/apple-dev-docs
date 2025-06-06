# calibratedLatency

**Framework**: UIKit  
**Kind**: property

The user-calibrated latency for the current screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+

## Declaration

```swift
@MainActor
var calibratedLatency: CFTimeInterval { get }
```

#### Discussion

Use this property when you need to manually synchronize video playback with custom audio. For example, you might correlate this value with the [`latency`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit/latency) property of a Core Audio unit when writing custom video-playback software. The value of this property is `0` until the user explicitly calibrates their display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/calibratedlatency)*