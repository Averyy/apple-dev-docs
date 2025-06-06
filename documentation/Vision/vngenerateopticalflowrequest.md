# VNGenerateOpticalFlowRequest

**Framework**: Vision  
**Kind**: class

An object that generates directional change vectors for each pixel in the targeted image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class VNGenerateOpticalFlowRequest
```

#### Overview

This request operates at a pixel level, so both images need to have the same dimensions to successfully perform the analysis. Setting a region of interest limits the region in which the analysis occurs. However, the system reports the resulting observation at full resolution.

Optical flow requests are resource-intensive, so create only one request at a time, and release it immediately after generating optical flows.

## Topics

### Configuring the Request
- [var computationAccuracy: VNGenerateOpticalFlowRequest.ComputationAccuracy](vngenerateopticalflowrequest/computationaccuracy-swift.property.md)
  The accuracy level for computing optical flow.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy](vngenerateopticalflowrequest/computationaccuracy-swift.enum.md)
  The supported optical flow accuracy levels.
- [var outputPixelFormat: OSType](vngenerateopticalflowrequest/outputpixelformat.md)
  The output buffer’s pixel format.
- [var keepNetworkOutput: Bool](vngenerateopticalflowrequest/keepnetworkoutput.md)
  A Boolean value that indicates whether to keep the raw pixel buffer coming from the machine learning network.
### Accessing the Results
- [var results: [VNPixelBufferObservation]?](vngenerateopticalflowrequest/results.md)
  The results of the request to generate optical flow.
### Identifying Request Revisions
- [let VNGenerateOpticalFlowRequestRevision2: Int](vngenerateopticalflowrequestrevision2.md)
  A constant for specifying revision 2 of the optical flow generation request.
- [let VNGenerateOpticalFlowRequestRevision1: Int](vngenerateopticalflowrequestrevision1.md)
  A constant for specifying revision 1 of the optical flow generation request.

## Relationships

### Inherits From
- [VNTargetedImageRequest](vntargetedimagerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VNTrackOpticalFlowRequest](vntrackopticalflowrequest.md)
  An object that determines the direction change of vectors for each pixel from a previous to current image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateopticalflowrequest)*