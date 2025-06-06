# addRequest(_:processingOptions:)

**Framework**: Vision  
**Kind**: method

Adds a request with processing options to the video processor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func addRequest(_ request: VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws
```

#### Discussion

Call this method either before calling [`analyze(_:)`](vnvideoprocessor/analyze(_:).md) or from within the completion handler of an already associated request.

## Parameters

- `request`: The Vision request to add.
- `processingOptions`: The processing options to apply.

## See Also

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
- [func analyze(with: CMTimeRange) throws](vnvideoprocessor/analyze(with:).md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/addrequest(_:processingoptions:))*