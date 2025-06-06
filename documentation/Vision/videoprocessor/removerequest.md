# removeRequest(_:)

**Framework**: Vision  
**Kind**: method

Stops performing a request on future frames.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final func removeRequest(_ request: any VisionRequest) async -> Bool
```

## Parameters

- `request`: The request to remove.

## See Also

- [func addRequest<T>(T, cadence: VideoProcessor.Cadence?) async throws -> some AsyncSequence<T.Result, any Error>
](videoprocessor/addrequest(_:cadence:).md)
  Adds a request to the video processor.
- [VideoProcessor.Cadence](videoprocessor/cadence.md)
  A type that describes the video processing cadence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/videoprocessor/removerequest(_:))*