# precisionEstimatesPerPoint

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

An array of precision estimates for each landmark point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```objc
@property (readonly, nullable) NSArray<NSNumber *> * precisionEstimatesPerPoint;
```

## Discussion

This property is only populated when you configure your [`VNDetectFaceLandmarksRequest`](../vndetectfacelandmarksrequest.md) object with [`VNRequestFaceLandmarksConstellation.constellation76Points`](../vnrequestfacelandmarksconstellation/constellation76points.md). For other constellation types, this array is set to `nil`.

## See Also

### Specifying Region Properties
- [normalizedPoints](./normalizedpoints-1o38f.md)
  A buffer in memory containing normalized landmark points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d/precisionestimatesperpoint-3kx5a)*