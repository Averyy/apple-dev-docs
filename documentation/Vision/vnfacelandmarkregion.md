# VNFaceLandmarkRegion

**Framework**: Vision  
**Kind**: class

The abstract superclass for information about a specific face landmark.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNFaceLandmarkRegion
```

## Topics

### Instance Properties
- [var pointCount: Int](vnfacelandmarkregion/pointcount.md)
  The number of points in the face region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [VNRequestRevisionProviding](vnrequestrevisionproviding.md)

## See Also

- [var landmarks: VNFaceLandmarks2D?](vnfaceobservation/landmarks.md)
  The facial features of the detected face.
- [class VNFaceLandmarks2D](vnfacelandmarks2d.md)
  A collection of facial features that a request detects.
- [class VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
  2D geometry information for a specific facial feature.
- [class VNFaceLandmarks](vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion)*