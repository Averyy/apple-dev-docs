# computationAccuracy

**Framework**: Vision  
**Kind**: property

The level of accuracy to compute the optical flow.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy { get set }
```

#### Discussion

The computational time trends with accuracy level. The default value is [`VNTrackOpticalFlowRequest.ComputationAccuracy.medium`](vntrackopticalflowrequest/computationaccuracy-swift.enum/medium.md).

## See Also

- [VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.enum.md)
  Computational accuracy options.
- [var keepNetworkOutput: Bool](vntrackopticalflowrequest/keepnetworkoutput.md)
  A Boolean value that indicates the raw pixel buffer continues to emit from the network.
- [var outputPixelFormat: OSType](vntrackopticalflowrequest/outputpixelformat.md)
  The pixel format type of the output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/computationaccuracy-swift.property)*