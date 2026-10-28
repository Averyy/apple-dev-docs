# addRequest(_:cadence:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Adds a request to the video processor.

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
final func addRequest<T>(_ request: T, cadence: VideoProcessor.Cadence? = nil) async throws -> some AsyncSequence<T.Result, any Error> where T : VisionRequest
```

## Return Value

An [`AsyncSequence`](../../Swift/asyncsequence.md) that produces a request result for each frame.

## Discussion

By default, the framework processes every frame.

## Parameters

- `request`: The request to perform.
- `cadence`: The cadency that specifies how to process the frames.

## See Also

### Adding and removing a request
- [VideoProcessor.Cadence](./cadence.md)
  A type that describes the video processing cadence.
- [func removeRequest(any VisionRequest) async -> Bool](./removerequest%28_%29.md)
  Stops performing a request on future frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/videoprocessor/addrequest(_:cadence:))*