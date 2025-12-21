# timeRange

**Framework**: Vision  
**Kind**: property

Time in a video frame where the observation was detected.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let timeRange: CMTimeRange?
```

#### Discussion

When evaluating a sequence of image buffers, use this property to determine each observation’s start time and duration.

## See Also

- [let uuid: UUID](documentobservation/uuid.md)
  A unique alphanumeric value that the framework assigns to the observation.
- [let confidence: Float](documentobservation/confidence.md)
  The level of confidence in the observation’s accuracy.
- [let document: DocumentObservation.Container](documentobservation/document.md)
  The contents of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/timerange)*