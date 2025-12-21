# minimumLatencyFrameCount

**Framework**: Vision  
**Kind**: property  
**Required**: Yes

The minimum number of frames that the request has to process before reporting any observations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var minimumLatencyFrameCount: Int { get }
```

#### Discussion

The request provides this information after it’s initialized with its required parameters.

Video-based requests often need a minimum number of frames before they can report any observations. For example, for movement detection that requires at least `5` frames, the [`minimumLatencyFrameCount`](statefulrequest/minimumlatencyframecount.md) for the request reports `5`, and after the request processes `5` frames, an observation returns the results.

## See Also

- [var frameAnalysisSpacing: CMTime](statefulrequest/frameanalysisspacing.md)
  The reciprocal of the maximum rate to process buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/statefulrequest/minimumlatencyframecount)*