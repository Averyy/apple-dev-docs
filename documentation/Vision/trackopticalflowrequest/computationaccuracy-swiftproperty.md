# computationAccuracy

**Framework**: Vision  
**Kind**: property

The level of accuracy to compute the optical flow.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final var computationAccuracy: TrackOpticalFlowRequest.ComputationAccuracy { get set }
```

#### Discussion

The computational time trends with accuracy level. The default value is [`TrackOpticalFlowRequest.ComputationAccuracy.high`](trackopticalflowrequest/computationaccuracy-swift.enum/high.md).

## See Also

- [TrackOpticalFlowRequest.ComputationAccuracy](trackopticalflowrequest/computationaccuracy-swift.enum.md)
  A type that describes the computational accuracy.
- [var outputPixelFormatType: OSType](trackopticalflowrequest/outputpixelformattype.md)
  The desired pixel format type of the observation.
- [var supportedOutputPixelFormatTypes: [OSType]](trackopticalflowrequest/supportedoutputpixelformattypes.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackopticalflowrequest/computationaccuracy-swift.property)*