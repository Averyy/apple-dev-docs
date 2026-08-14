# outputPixelFormat

**Framework**: Vision  
**Kind**: property

The pixel format type of the output value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var outputPixelFormat: OSType { get set }
```

#### Discussion

The valid values are [`kCVPixelFormatType_TwoComponent32Float`](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_twocomponent32float) and [`kCVPixelFormatType_TwoComponent16Half`](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_twocomponent16half). The default value is [`kCVPixelFormatType_TwoComponent32Float`](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_twocomponent32float).

## See Also

- [var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [VNTrackOpticalFlowRequest.ComputationAccuracy](vntrackopticalflowrequest/computationaccuracy-swift.enum.md)
  Computational accuracy options.
- [var keepNetworkOutput: Bool](vntrackopticalflowrequest/keepnetworkoutput.md)
  A Boolean value that indicates the raw pixel buffer continues to emit from the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/outputpixelformat)*