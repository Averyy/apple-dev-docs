# timeRange

**Framework**: Vision  
**Kind**: property

The time range of the reported observation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

When evaluating a sequence of image buffers, use this property to determine each observation’s start time and duration. If a request doesn’t support time ranges, or the time range is unknown, the value of this property is [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange/zero).

## See Also

- [var confidence: VNConfidence](vnobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [typealias VNConfidence](vnconfidence.md)
  A type alias for the confidence value of an observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnobservation/timerange)*