# calibratedLatency

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The user-calibrated latency for the current screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+

## Declaration

```swift
var calibratedLatency: CFTimeInterval { get }
```

```objc
@property (nonatomic, readonly) CFTimeInterval calibratedLatency;
```

## Discussion

Use this property when you need to manually synchronize video playback with custom audio. For example, you might correlate this value with the [`latency`](../../AudioToolbox/auaudiounit/latency.md) property of a Core Audio unit when writing custom video-playback software. The value of this property is `0` until the user explicitly calibrates their display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/calibratedlatency)*