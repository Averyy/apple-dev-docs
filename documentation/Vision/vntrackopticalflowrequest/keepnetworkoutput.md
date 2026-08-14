# keepNetworkOutput

**Framework**: Vision  
**Kind**: property

A Boolean value that indicates the raw pixel buffer continues to emit from the network.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var keepNetworkOutput: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false); otherwise, the request ignores [`outputPixelFormat`](vntrackopticalflowrequest/outputpixelformat.md).

## See Also

- [var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.enum.md)
  Computational accuracy options.
- [var outputPixelFormat: OSType](vntrackopticalflowrequest/outputpixelformat.md)
  The pixel format type of the output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/keepnetworkoutput)*