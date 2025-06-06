# VNGenerateOpticalFlowRequest.ComputationAccuracy

**Framework**: Vision  
**Kind**: enum

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

#### Overview

The computation time typically increases with accuracy.

## Topics

### Accuracy Levels
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.low](vngenerateopticalflowrequest/computationaccuracy-swift.enum/low.md)
  Low accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.medium](vngenerateopticalflowrequest/computationaccuracy-swift.enum/medium.md)
  Medium accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.high](vngenerateopticalflowrequest/computationaccuracy-swift.enum/high.md)
  High accuracy.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy.veryHigh](vngenerateopticalflowrequest/computationaccuracy-swift.enum/veryhigh.md)
  Very high accuracy.
### Creating an Accuracy Level
- [init?(rawValue: UInt)](vngenerateopticalflowrequest/computationaccuracy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var computationAccuracy: VNGenerateOpticalFlowRequest.ComputationAccuracy](vngenerateopticalflowrequest/computationaccuracy-swift.property.md)
  The accuracy level for computing optical flow.
- [var outputPixelFormat: OSType](vngenerateopticalflowrequest/outputpixelformat.md)
  The output buffer’s pixel format.
- [var keepNetworkOutput: Bool](vngenerateopticalflowrequest/keepnetworkoutput.md)
  A Boolean value that indicates whether to keep the raw pixel buffer coming from the machine learning network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateopticalflowrequest/computationaccuracy-swift.enum)*