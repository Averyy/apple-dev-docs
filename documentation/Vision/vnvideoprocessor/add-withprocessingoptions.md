# add(_:withProcessingOptions:)

**Framework**: Vision  
**Kind**: method

Adds a Vision request to perform with the specified configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ request: VNRequest, withProcessingOptions processingOptions: [VNVideoProcessingOption : Any] = [:]) throws
```

## Parameters

- `request`: The request to add to the processing queue.
- `processingOptions`: The options to use for processing.

## Topics

### Video Processing Options
- [struct VNVideoProcessingOption](vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.

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
- [func analyze(with: CMTimeRange) throws](vnvideoprocessor/analyze(with:).md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/add(_:withprocessingoptions:))*