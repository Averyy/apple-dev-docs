# VNTrackOpticalFlowRequest

**Framework**: Vision  
**Kind**: class

An object that determines the direction change of vectors for each pixel from a previous to current image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class VNTrackOpticalFlowRequest
```

#### Overview

This request works at the pixel level, so both images must have the same dimensions to successfully perform the request.

Setting a region of interest isolates where to perform the change determination.

> ❗ **Important**:  Optical flow requests are very resource intensive, so perform only one request at a time. Release memory immediately after generating an optical flow.

 Optical flow requests are very resource intensive, so perform only one request at a time. Release memory immediately after generating an optical flow.

## Topics

### Creating an Optical Flow
- [init()](vntrackopticalflowrequest/init.md)
  Creates a new request that tracks the optical from one image to another.
- [init(completionHandler: VNRequestCompletionHandler?)](vntrackopticalflowrequest/init(completionhandler:).md)
  Creates a new request that tracks the optical from one image to another, with a system callback on completion.
### Configuring the Request
- [var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.enum.md)
  Computational accuracy options.
- [var keepNetworkOutput: Bool](vntrackopticalflowrequest/keepnetworkoutput.md)
  A Boolean value that indicates the raw pixel buffer continues to emit from the network.
- [var outputPixelFormat: OSType](vntrackopticalflowrequest/outputpixelformat.md)
  The pixel format type of the output value.
### Accessing the Results
- [var results: [VNPixelBufferObservation]?](vntrackopticalflowrequest/results.md)
  The optical flow results the request observes.

## Relationships

### Inherits From
- [VNStatefulRequest](vnstatefulrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VNGenerateOpticalFlowRequest](vngenerateopticalflowrequest.md)
  An object that generates directional change vectors for each pixel in the targeted image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest)*