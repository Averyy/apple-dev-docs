# VNFaceObservation

**Framework**: Vision  
**Kind**: class

Face or facial-feature information that an image analysis request detects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class VNFaceObservation
```

#### Overview

This type of observation results from a [`VNDetectFaceRectanglesRequest`](vndetectfacerectanglesrequest.md). It contains information about facial landmarks and regions it finds in the image.

## Topics

### Creating an Observation
- [convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?, pitch: NSNumber?)](vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:pitch:).md)
  Creates an observation that contains the roll, yaw, and pitch of the face.
- [convenience init(requestRevision: Int, boundingBox: CGRect, roll: NSNumber?, yaw: NSNumber?)](vnfaceobservation/init(requestrevision:boundingbox:roll:yaw:).md)
  Creates an observation that contains the roll and yaw of the face.
### Identifying Landmarks
- [var landmarks: VNFaceLandmarks2D?](vnfaceobservation/landmarks.md)
  The facial features of the detected face.
- [class VNFaceLandmarks2D](vnfacelandmarks2d.md)
  A collection of facial features that a request detects.
- [class VNFaceLandmarkRegion2D](vnfacelandmarkregion2d.md)
  2D geometry information for a specific facial feature.
- [class VNFaceLandmarks](vnfacelandmarks.md)
  The abstract superclass for containers of face landmark information.
- [class VNFaceLandmarkRegion](vnfacelandmarkregion.md)
  The abstract superclass for information about a specific face landmark.
### Determining Facial Orientation
- [var roll: NSNumber?](vnfaceobservation/roll.md)
  The roll angle of a face in radians.
- [var yaw: NSNumber?](vnfaceobservation/yaw.md)
  The yaw angle of a face in radians.
- [var pitch: NSNumber?](vnfaceobservation/pitch.md)
  The pitch angle of a face in radians.
### Determining Capture Quality
- [var faceCaptureQuality: Float?](vnfaceobservation/facecapturequality-bjg5.md)
  A value that indicates the quality of the face capture.

## Relationships

### Inherits From
- [VNDetectedObjectObservation](vndetectedobjectobservation.md)
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

- [var results: [VNFaceObservation]?](vndetectfacecapturequalityrequest/results.md)
  The results of the face-capture quality request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation)*