# analyze(with:)

**Framework**: Vision  
**Kind**: method

Analyzes the specifed time range of the video content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func analyze(with timeRange: CMTimeRange) throws
```

#### Discussion

The system executes this method synchronously, so you should typically call it from a separate dispatch queue. It returns when the video processor finishes analyzing the specified time range, or if an error prevented the processing.

## Parameters

- `timeRange`: The time range to analyze. The value specified must be within the time range of the video asset.

## See Also

- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](vnvideoprocessor/addrequest(_:processingoptions:).md)
  Adds a request with processing options to the video processor.
- [VNVideoProcessor.RequestProcessingOptions](vnvideoprocessor/requestprocessingoptions.md)
  An object that defines a video processor’s configuration options.
- [func removeRequest(VNRequest) throws](vnvideoprocessor/removerequest(_:).md)
  Removes a Vision request from the video processor’s request queue.
- [func analyze(CMTimeRange) throws](vnvideoprocessor/analyze(_:).md)
  Analyzes a time range of video content.
- [func cancel()](vnvideoprocessor/cancel.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](vnvideoprocessor/add(_:withprocessingoptions:).md)
  Adds a Vision request to perform with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/analyze(with:))*