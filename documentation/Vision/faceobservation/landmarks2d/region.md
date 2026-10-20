# FaceObservation.Landmarks2D.Region

**Framework**: Vision  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
struct Region
```

## Topics

### Inspecting a region
- [let originatingRequestDescriptor: RequestDescriptor?](./region/originatingrequestdescriptor.md)
- [let points: [NormalizedPoint]](./region/points.md)
- [let pointsClassification: FaceObservation.Landmarks2D.Region.PointsClassification](./region/pointsclassification-swift.property.md)
- [FaceObservation.Landmarks2D.Region.PointsClassification](./region/pointsclassification-swift.enum.md)
- [let precisionEstimatesPerPoint: [Float]?](./region/precisionestimatesperpoint.md)
### Getting the points
- [func pointsInImageCoordinates(CGSize, origin: CoordinateOrigin) -> [CGPoint]](./region/pointsinimagecoordinates%28_,origin%29.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting all landmarks
- [var allPoints: FaceObservation.Landmarks2D.Region](./allpoints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks2d/region)*