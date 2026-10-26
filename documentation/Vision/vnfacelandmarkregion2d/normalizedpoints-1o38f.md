# normalizedPoints

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A buffer in memory containing normalized landmark points.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
@property (assign, readonly, nullable) const CGPoint * normalizedPoints;
```

#### Discussion

This pointer points to the address of a buffer containing [`CGPoint`](../../CoreFoundation/cgpoint.md) structs representing landmark points.

The target object owns this buffer, which is guaranteed to exist as long as the corresponding [`VNFaceLandmarkRegion2D`](../vnfacelandmarkregion2d.md) exists.

## See Also

### Specifying Region Properties
- [precisionEstimatesPerPoint](./precisionestimatesperpoint-3kx5a.md)
  An array of precision estimates for each landmark point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d/normalizedpoints-1o38f)*