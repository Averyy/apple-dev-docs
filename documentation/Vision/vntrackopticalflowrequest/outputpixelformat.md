# outputPixelFormat

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign, readwrite) OSType outputPixelFormat;
```

## Discussion

The valid values are [`kCVPixelFormatType_TwoComponent32Float`](../../CoreVideo/kcvpixelformattype_twocomponent32float.md) and [`kCVPixelFormatType_TwoComponent16Half`](../../CoreVideo/kcvpixelformattype_twocomponent16half.md). The default value is [`kCVPixelFormatType_TwoComponent32Float`](../../CoreVideo/kcvpixelformattype_twocomponent32float.md).

## See Also

### Configuring the Request
- [var computationAccuracy: VNTrackOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [VNTrackOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.enum.md)
  Computational accuracy options.
- [var keepNetworkOutput: Bool](./keepnetworkoutput.md)
  A Boolean value that indicates the raw pixel buffer continues to emit from the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackopticalflowrequest/outputpixelformat)*