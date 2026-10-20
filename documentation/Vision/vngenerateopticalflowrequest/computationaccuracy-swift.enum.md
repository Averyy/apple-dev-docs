# VNGenerateOpticalFlowRequest.ComputationAccuracy

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

The supported optical flow accuracy levels.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum ComputationAccuracy
```

```c
enum VNGenerateOpticalFlowRequestComputationAccuracy : NSUInteger;
```

#### Overview

The computation time typically increases with accuracy.

## Topics

### Accuracy Levels
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.low](./computationaccuracy-swift.enum/low.md)
  Low accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.medium](./computationaccuracy-swift.enum/medium.md)
  Medium accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.high](./computationaccuracy-swift.enum/high.md)
  High accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.veryHigh](./computationaccuracy-swift.enum/veryhigh.md)
  Very high accuracy.
### Creating an Accuracy Level
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
- [var computationAccuracy: VNGenerateOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.property.md)
  The accuracy level for computing optical flow.
- [var outputPixelFormat: OSType](./outputpixelformat.md)
  The output buffer’s pixel format.
- [var keepNetworkOutput: Bool](./keepnetworkoutput.md)
  A Boolean value that indicates whether to keep the raw pixel buffer coming from the machine learning network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateopticalflowrequest/computationaccuracy-swift.enum)*