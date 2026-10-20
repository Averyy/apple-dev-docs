# VideoProcessor.Cadence

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

A type that describes the video processing cadence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
enum Cadence
```

## Topics

### Getting the intervals
- [VideoProcessor.Cadence.timeInterval(_:)](./cadence/timeinterval%28_%29.md)
  A cadence that processes, at most, one frame during each interval you specify.
- [VideoProcessor.Cadence.frameInterval(_:)](./cadence/frameinterval%28_%29.md)
  A cadence that processes every frame you specify.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Adding and removing a request
- [func addRequest<T>(T, cadence: VideoProcessor.Cadence?) async throws -> some AsyncSequence<T.Result, any Error>
](./addrequest%28_,cadence%29.md)
  Adds a request to the video processor.
- [func removeRequest(any VisionRequest) async -> Bool](./removerequest%28_%29.md)
  Stops performing a request on future frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/videoprocessor/cadence)*