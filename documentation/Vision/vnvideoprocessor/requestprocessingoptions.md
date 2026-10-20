# VNVideoProcessor.RequestProcessingOptions

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNVideoProcessorRequestProcessingOptions : NSObject
```

## Topics

### Configuring Options
- [var cadence: VNVideoProcessor.Cadence?](./requestprocessingoptions/cadence.md)
  The cadence the video processor maintains to process the request.
- [VNVideoProcessor.Cadence](./cadence.md)
  An object that defines the cadence at which to process video.
- [VNVideoProcessor.FrameRateCadence](./frameratecadence.md)
  An object that defines a frame-based cadence for processing a video stream.
- [VNVideoProcessor.TimeIntervalCadence](./timeintervalcadence.md)
  An object that defines a time-based cadence for processing a video stream.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Performing Requests
- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](./addrequest%28_,processingoptions%29.md)
  Adds a request with processing options to the video processor.
- [func removeRequest(VNRequest) throws](./removerequest%28_%29.md)
  Removes a Vision request from the video processor’s request queue.
- [func analyze(CMTimeRange) throws](./analyze%28_%29.md)
  Analyzes a time range of video content.
- [func cancel()](./cancel%28%29.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](./add%28_,withprocessingoptions%29.md)
  Adds a Vision request to perform with the specified configuration.
- [func analyze(with: CMTimeRange) throws](./analyze%28with%29.md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/requestprocessingoptions)*