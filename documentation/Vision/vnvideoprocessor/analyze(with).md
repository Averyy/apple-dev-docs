# analyze(with:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Analyzes the specifed time range of the video content.

**Availability**:
- iOS 14.0+ - Deprecated in 14.0
- iPadOS 14.0+ - Deprecated in 14.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 11.0+ - Deprecated in 11.0
- tvOS 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`analyze(_:)`](./analyze%28_%29.md) instead.

## Declaration

```swift
func analyze(with timeRange: CMTimeRange) throws
```

```objc
- (BOOL) analyzeWithTimeRange:(CMTimeRange) timeRange error:(NSError **) error;
```

#### Discussion

The system executes this method synchronously, so you should typically call it from a separate dispatch queue. It returns when the video processor finishes analyzing the specified time range, or if an error prevented the processing.

## Parameters

- `timeRange`: The time range to analyze. The value specified must be within the time range of the video asset.

## See Also

### Performing Requests
- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](./addrequest%28_,processingoptions%29.md)
  Adds a request with processing options to the video processor.
- [VNVideoProcessor.RequestProcessingOptions](./requestprocessingoptions.md)
  An object that defines a video processor’s configuration options.
- [func removeRequest(VNRequest) throws](./removerequest%28_%29.md)
  Removes a Vision request from the video processor’s request queue.
- [func analyze(CMTimeRange) throws](./analyze%28_%29.md)
  Analyzes a time range of video content.
- [func cancel()](./cancel%28%29.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](./add%28_,withprocessingoptions%29.md)
  Adds a Vision request to perform with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/analyze(with:))*