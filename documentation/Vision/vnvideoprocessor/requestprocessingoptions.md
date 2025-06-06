# VNVideoProcessor.RequestProcessingOptions

**Framework**: Vision  
**Kind**: class

An object that defines a video processor’s configuration options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class RequestProcessingOptions
```

## Topics

### Configuring Options
- [var cadence: VNVideoProcessor.Cadence?](vnvideoprocessor/requestprocessingoptions/cadence.md)
  The cadence the video processor maintains to process the request.
- [VNVideoProcessor.Cadence](vnvideoprocessor/cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.FrameRateCadence](vnvideoprocessor/frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.
- [VNVideoProcessor.TimeIntervalCadence](vnvideoprocessor/timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](vnvideoprocessor/addrequest(_:processingoptions:).md)
  Adds a request with processing options to the video processor.
- [func removeRequest(VNRequest) throws](vnvideoprocessor/removerequest(_:).md)
  Removes a Vision request from the video processor’s request queue.
- [func analyze(CMTimeRange) throws](vnvideoprocessor/analyze(_:).md)
  Analyzes a time range of video content.
- [func cancel()](vnvideoprocessor/cancel.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](vnvideoprocessor/add(_:withprocessingoptions:).md)
  Adds a Vision request to perform with the specified configuration.
- [func analyze(with: CMTimeRange) throws](vnvideoprocessor/analyze(with:).md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/requestprocessingoptions)*