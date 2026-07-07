# precisionEstimatesPerPoint

**Framework**: Vision  
**Kind**: property

Requests an array of precision estimates for each landmark point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
@nonobjc
var precisionEstimatesPerPoint: [Float]? { get }
```

#### Discussion

This property is only populated when you configure your [`VNDetectFaceLandmarksRequest`](vndetectfacelandmarksrequest.md) object with [`VNRequestFaceLandmarksConstellation.constellation76Points`](vnrequestfacelandmarksconstellation/constellation76points.md). For other constellation types, this array is set to `nil`.

## See Also

- [var normalizedPoints: [CGPoint]](vnfacelandmarkregion2d/normalizedpoints-7s7im.md)
  The array of normalized landmark points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d/precisionestimatesperpoint-5jl22)*