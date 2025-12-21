# VNVideoProcessor

**Framework**: Vision  
**Kind**: class

An object that performs offline analysis of video content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNVideoProcessor
```

## Topics

### Creating a Video Processor
- [init(url: URL)](vnvideoprocessor/init(url:).md)
  Creates a video processor to perform Vision requests against the specified video asset.
### Performing Requests
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
- [func analyze(with: CMTimeRange) throws](vnvideoprocessor/analyze(with:).md)
  Analyzes the specifed time range of the video content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct VNComputeStage](vncomputestage.md)
  Types that represent the compute stage.
- [class VNGeometryUtils](vngeometryutils.md)
  Utility methods to determine the geometries of various Vision types.
- [struct VNVideoProcessingOption](vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor)*