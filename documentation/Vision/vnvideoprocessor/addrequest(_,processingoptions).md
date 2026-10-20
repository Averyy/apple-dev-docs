# addRequest(_:processingOptions:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) addRequest:(VNRequest *) request processingOptions:(VNVideoProcessorRequestProcessingOptions *) processingOptions error:(NSError **) error;
```

#### Discussion

Call this method either before calling [`analyze(_:)`](./analyze%28_%29.md) or from within the completion handler of an already associated request.

## Parameters

- `request`: The Vision request to add.
- `processingOptions`: The processing options to apply.

## See Also

### Performing Requests
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
- [func analyze(with: CMTimeRange) throws](./analyze%28with%29.md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/addrequest(_:processingoptions:))*