# VNFaceLandmarkRegion

**Framework**: Vision  
**Kind**: class  
**Role**: Class

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

```objc
@interface VNFaceLandmarkRegion : NSObject
```

## Topics

### Creating a Region
- [init?(coder: NSCoder)](./vnfacelandmarkregion/init%28coder%29.md)
### Getting the Count
- [var pointCount: Int](./vnfacelandmarkregion/pointcount.md)
  The number of points in the face region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VNFaceLandmarkRegion2D](./vnfacelandmarkregion2d.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [VNRequestRevisionProviding](./vnrequestrevisionproviding.md)

## See Also

### Identifying Landmarks
- [var landmarks: VNFaceLandmarks2D?](./vnfaceobservation/landmarks.md)
  The facial features of the detected face.
- [class VNFaceLandmarks2D](./vnfacelandmarks2d.md)
  A collection of facial features that a request detects.
- [class VNFaceLandmarkRegion2D](./vnfacelandmarkregion2d.md)
  2D geometry information for a specific facial feature.
- [class VNFaceLandmarks](./vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfacelandmarkregion)*