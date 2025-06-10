# VideoProcessor

**Framework**: Vision  
**Kind**: class

An object that performs offline analysis of video content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final class VideoProcessor
```

## Topics

### Creating a video processor
- [init(URL)](videoprocessor/init(_:).md)
  Creates a video processor to perform framework requests against the video asset you specify.
### Adding and removing a request
- [func addRequest<T>(T, cadence: VideoProcessor.Cadence?) async throws -> some AsyncSequence<T.Result, any Error>
](videoprocessor/addrequest(_:cadence:).md)
  Adds a request to the video processor.
- [VideoProcessor.Cadence](videoprocessor/cadence.md)
  A type that describes the video processing cadence.
- [func removeRequest(any VisionRequest) async -> Bool](videoprocessor/removerequest(_:).md)
  Stops performing a request on future frames.
### Starting the analysis
- [func startAnalysis(of: CMTimeRange?)](videoprocessor/startanalysis(of:).md)
  Begins analyzing video frames.
### Cancelling the analysis
- [func cancel() async](videoprocessor/cancel.md)
  Stops the video processor.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ComputeStage](computestage.md)
  Types that represent the compute stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/videoprocessor)*