# frameAnalysisSpacing

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The reciprocal of the maximum rate to process buffers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var frameAnalysisSpacing: CMTime { get }
```

#### Discussion

The request won’t process buffers that fall within the [`frameAnalysisSpacing`](statefulrequest/frameanalysisspacing.md) since the previously performed analysis. The analysis isn’t done by wall time but by analysis of the time stamps of the sample buffers the request processes.

## See Also

- [var minimumLatencyFrameCount: Int](statefulrequest/minimumlatencyframecount.md)
  The minimum number of frames that the request has to process before reporting any observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/statefulrequest/frameanalysisspacing)*