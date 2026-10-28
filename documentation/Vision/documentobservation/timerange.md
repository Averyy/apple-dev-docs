# timeRange

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

Time in a video frame where the observation was detected.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let timeRange: CMTimeRange?
```

## Discussion

When evaluating a sequence of image buffers, use this property to determine each observation’s start time and duration.

## See Also

### Inspecting an observation
- [let uuid: UUID](./uuid.md)
  A unique alphanumeric value that the framework assigns to the observation.
- [let confidence: Float](./confidence.md)
  The level of confidence in the observation’s accuracy.
- [let document: DocumentObservation.Container](./document.md)
  The contents of the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/timerange)*