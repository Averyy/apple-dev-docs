# VNHumanObservation

**Framework**: Vision  
**Kind**: class  
**Role**: Class

An object that represents a person that the request detects.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class VNHumanObservation
```

```objc
@interface VNHumanObservation : VNDetectedObjectObservation
```

## Topics

### Inspecting the Observation
- [var upperBodyOnly: Bool](./vnhumanobservation/upperbodyonly.md)
  A Boolean value that indicates whether the observation represents an upper-body or full-body rectangle.

## Relationships

### Inherits From
- [VNDetectedObjectObservation](./vndetectedobjectobservation.md)
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

### Face and body detection
- [Selecting a selfie based on capture quality](./selecting-a-selfie-based-on-capture-quality.md)
  Compare face-capture quality in a set of images by using Vision.
- [class VNDetectFaceCaptureQualityRequest](./vndetectfacecapturequalityrequest.md)
  A request that produces a floating-point number that represents the capture quality of a face in a photo.
- [class VNDetectFaceLandmarksRequest](./vndetectfacelandmarksrequest.md)
  An image-analysis request that finds facial features like eyes and mouth in an image.
- [class VNDetectFaceRectanglesRequest](./vndetectfacerectanglesrequest.md)
  A request that finds faces within an image.
- [class VNDetectHumanRectanglesRequest](./vndetecthumanrectanglesrequest.md)
  A request that finds rectangular regions that contain people in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanobservation)*