# VNTrackOpticalFlowRequest.ComputationAccuracy

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Computational accuracy options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum ComputationAccuracy
```

```c
enum VNTrackOpticalFlowRequestComputationAccuracy : NSUInteger;
```

## Topics

### Options
- [VNTrackOpticalFlowRequest.ComputationAccuracy.low](./computationaccuracy-swift.enum/low.md)
  An option that indicates a low level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.medium](./computationaccuracy-swift.enum/medium.md)
  An option that indicates a moderate level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.high](./computationaccuracy-swift.enum/high.md)
  An option that indicates a high level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.veryHigh](./computationaccuracy-swift.enum/veryhigh.md)
  An option that indicates a very high level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.low](./computationaccuracy-swift.enum/low.md)
  An option that indicates a low level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.medium](./computationaccuracy-swift.enum/medium.md)
  An option that indicates a moderate level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.high](./computationaccuracy-swift.enum/high.md)
  An option that indicates a high level of computational accuracy.
- [VNTrackOpticalFlowRequest.ComputationAccuracy.veryHigh](./computationaccuracy-swift.enum/veryhigh.md)
  An option that indicates a very high level of computational accuracy.
### Creating an Accuracy Option
- [init?(rawValue: UInt)](./computationaccuracy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Request
- [var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [var keepNetworkOutput: Bool](./keepnetworkoutput.md)
  A Boolean value that indicates the raw pixel buffer continues to emit from the network.
- [var outputPixelFormat: OSType](./outputpixelformat.md)
  The pixel format type of the output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/computationaccuracy-swift.enum)*