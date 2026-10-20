# computationAccuracy

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The accuracy level for computing optical flow.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var computationAccuracy: VNGenerateOpticalFlowRequest.ComputationAccuracy { get set }
```

```objc
@property (nonatomic, assign, readwrite) VNGenerateOpticalFlowRequestComputationAccuracy computationAccuracy;
```

## See Also

### Configuring the Request
- [VNGenerateOpticalFlowRequest.ComputationAccuracy](./computationaccuracy-swift.enum.md)
  The supported optical flow accuracy levels.
- [var outputPixelFormat: OSType](./outputpixelformat.md)
  The output buffer’s pixel format.
- [var keepNetworkOutput: Bool](./keepnetworkoutput.md)
  A Boolean value that indicates whether to keep the raw pixel buffer coming from the machine learning network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngenerateopticalflowrequest/computationaccuracy-swift.property)*