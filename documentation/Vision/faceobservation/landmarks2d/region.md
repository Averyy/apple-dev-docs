# FaceObservation.Landmarks2D.Region

**Framework**: Vision  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Region
```

## Topics

### Inspecting a region
- [let originatingRequestDescriptor: RequestDescriptor?](faceobservation/landmarks2d/region/originatingrequestdescriptor.md)
- [let points: [NormalizedPoint]](faceobservation/landmarks2d/region/points.md)
- [let pointsClassification: FaceObservation.Landmarks2D.Region.PointsClassification](faceobservation/landmarks2d/region/pointsclassification-swift.property.md)
- [FaceObservation.Landmarks2D.Region.PointsClassification](faceobservation/landmarks2d/region/pointsclassification-swift.enum.md)
- [let precisionEstimatesPerPoint: [Float]?](faceobservation/landmarks2d/region/precisionestimatesperpoint.md)
### Getting the points
- [func pointsInImageCoordinates(CGSize, origin: CoordinateOrigin) -> [CGPoint]](faceobservation/landmarks2d/region/pointsinimagecoordinates(_:origin:).md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var allPoints: FaceObservation.Landmarks2D.Region](faceobservation/landmarks2d/allpoints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/landmarks2d/region)*