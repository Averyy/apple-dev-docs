# confidence

**Framework**: Vision  
**Kind**: property

The level of confidence in the observation’s accuracy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let confidence: Float
```

#### Discussion

The framework normalizes this value to `[0, 1]`, where `1` represents the most confident in the observation’s accuracy.

## See Also

- [let uuid: UUID](documentobservation/uuid.md)
  A unique alphanumeric value that the framework assigns to the observation.
- [let document: DocumentObservation.Container](documentobservation/document.md)
  The contents of the document.
- [let timeRange: CMTimeRange?](documentobservation/timerange.md)
  Time in a video frame where the observation was detected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/documentobservation/confidence)*