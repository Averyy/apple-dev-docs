# add(_:withProcessingOptions:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Adds a Vision request to perform with the specified configuration.

**Availability**:
- iOS 14.0+ - Deprecated in 14.0
- iPadOS 14.0+ - Deprecated in 14.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 11.0+ - Deprecated in 11.0
- tvOS 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`addRequest(_:processingOptions:)`](./addrequest%28_,processingoptions%29.md) instead.

## Declaration

```swift
func add(_ request: VNRequest, withProcessingOptions processingOptions: [VNVideoProcessingOption : Any] = [:]) throws
```

```objc
- (BOOL) addRequest:(VNRequest *) request withProcessingOptions:(NSDictionary<NSString *,id> *) processingOptions error:(NSError **) error;
```

## Parameters

- `request`: The request to add to the processing queue.
- `processingOptions`: The options to use for processing.

## Topics

### Video Processing Options
- [struct VNVideoProcessingOption](../vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.

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
- [func analyze(with: CMTimeRange) throws](./analyze%28with%29.md)
  Analyzes the specifed time range of the video content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor/add(_:withprocessingoptions:))*