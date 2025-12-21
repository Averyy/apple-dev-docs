# VideoProcessor.Cadence

**Framework**: Vision  
**Kind**: enum

A type that describes the video processing cadence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Cadence
```

## Topics

### Getting the intervals
- [VideoProcessor.Cadence.timeInterval(_:)](videoprocessor/cadence/timeinterval(_:).md)
  A cadence that processes, at most, one frame during each interval you specify.
- [VideoProcessor.Cadence.frameInterval(_:)](videoprocessor/cadence/frameinterval(_:).md)
  A cadence that processes every frame you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func addRequest<T>(T, cadence: VideoProcessor.Cadence?) async throws -> some AsyncSequence<T.Result, any Error>
](videoprocessor/addrequest(_:cadence:).md)
  Adds a request to the video processor.
- [func removeRequest(any VisionRequest) async -> Bool](videoprocessor/removerequest(_:).md)
  Stops performing a request on future frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/videoprocessor/cadence)*