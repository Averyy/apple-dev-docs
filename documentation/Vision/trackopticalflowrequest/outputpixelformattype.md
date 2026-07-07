# outputPixelFormatType

**Framework**: Vision  
**Kind**: property

The desired pixel format type of the observation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final var outputPixelFormatType: OSType { get set }
```

#### Discussion

The default is [`kCVPixelFormatType_TwoComponent32Float`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_TwoComponent32Float).

## See Also

- [var computationAccuracy: TrackOpticalFlowRequest.ComputationAccuracy](trackopticalflowrequest/computationaccuracy-swift.property.md)
  The level of accuracy to compute the optical flow.
- [TrackOpticalFlowRequest.ComputationAccuracy](trackopticalflowrequest/computationaccuracy-swift.enum.md)
  A type that describes the computational accuracy.
- [var supportedOutputPixelFormatTypes: [OSType]](trackopticalflowrequest/supportedoutputpixelformattypes.md)
  The collection of supported pixel format types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/trackopticalflowrequest/outputpixelformattype)*