# VNVideoProcessor

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNVideoProcessor : NSObject
```

## Topics

### Creating a Video Processor
- [init(URL: URL)](./vnvideoprocessor/init%28url%29-38vj9.md)
- [init(url: URL)](./vnvideoprocessor/init%28url%29-94b7.md)
  Creates a video processor to perform Vision requests against the specified video asset.
### Performing Requests
- [func addRequest(VNRequest, processingOptions: VNVideoProcessor.RequestProcessingOptions) throws](./vnvideoprocessor/addrequest%28_,processingoptions%29.md)
  Adds a request with processing options to the video processor.
- [VNVideoProcessor.RequestProcessingOptions](./vnvideoprocessor/requestprocessingoptions.md)
  An object that defines a video processor’s configuration options.
- [func removeRequest(VNRequest) throws](./vnvideoprocessor/removerequest%28_%29.md)
  Removes a Vision request from the video processor’s request queue.
- [func analyze(CMTimeRange) throws](./vnvideoprocessor/analyze%28_%29.md)
  Analyzes a time range of video content.
- [func cancel()](./vnvideoprocessor/cancel%28%29.md)
  Cancels the video processing.
- [func add(VNRequest, withProcessingOptions: [VNVideoProcessingOption : Any]) throws](./vnvideoprocessor/add%28_,withprocessingoptions%29.md)
  Adds a Vision request to perform with the specified configuration.
- [func analyze(with: CMTimeRange) throws](./vnvideoprocessor/analyze%28with%29.md)
  Analyzes the specifed time range of the video content.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Utilities
- [struct VNComputeStage](./vncomputestage.md)
  Types that represent the compute stage.
- [class VNGeometryUtils](./vngeometryutils.md)
  Utility methods to determine the geometries of various Vision types.
- [struct VNVideoProcessingOption](./vnvideoprocessingoption.md)
  Options to pass to the video processor when adding requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnvideoprocessor)*