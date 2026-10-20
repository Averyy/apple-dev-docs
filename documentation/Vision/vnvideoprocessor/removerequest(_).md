# removeRequest(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Removes a Vision request from the video processor’s request queue.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeRequest(_ request: VNRequest) throws
```

```objc
- (BOOL) removeRequest:(VNRequest *) request error:(NSError **) error;
```

## Parameters

- `request`: The request to remove.

## See Also

### Performing Requests
- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](./addrequest%28_,processingoptions%29.md)
  Adds a request with processing options to the video processor.
- [VNVideoProcessor.RequestProcessingOptions](./requestprocessingoptions.md)
  An object that defines a video processor’s configuration options.
- [func analyze(CMTimeRange) throws](./analyze%28_%29.md)
  Analyzes a time range of video content.
- [func cancel()](./cancel%28%29.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](./add%28_,withprocessingoptions%29.md)
  Adds a Vision request to perform with the specified configuration.
- [func analyze(with: CMTimeRange) throws](./analyze%28with%29.md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/removerequest(_:))*