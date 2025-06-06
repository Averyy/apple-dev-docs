# minimumLatencyFrameCount

**Framework**: Vision  
**Kind**: property

The minimum number of frames a request processes before reporting an observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var minimumLatencyFrameCount: Int { get }
```

#### Discussion

Video-based requests often need a minimum number of frames before they can report an observation. For example, a movement detection request requires a minimum of five frames before it can generate an observation. This value indicates how responsive a request is at processing incoming data.

## See Also

- [var frameAnalysisSpacing: CMTime](vnstatefulrequest/frameanalysisspacing.md)
  A time value that indicates the interval between analysis operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnstatefulrequest/minimumlatencyframecount)*