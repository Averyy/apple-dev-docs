# keepNetworkOutput

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to keep the raw pixel buffer coming from the machine learning network.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var keepNetworkOutput: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL keepNetworkOutput;
```

## Discussion

The default is [`false`](../../Swift/false.md). When you set this to [`true`](../../Swift/true.md), the system ignores [`outputPixelFormat`](./outputpixelformat.md). Setting this for revision 1 has no effect because it’s not machine learning-based.

## See Also

### Configuring the Request
- [var computationAccuracy: VNGenerateOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.property.md)
  The accuracy level for computing optical flow.
- [VNGenerateOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.enum.md)
  The supported optical flow accuracy levels.
- [var outputPixelFormat: OSType](./outputpixelformat.md)
  The output buffer’s pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateopticalflowrequest/keepnetworkoutput)*