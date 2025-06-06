# pointInImage(_:)

**Framework**: Vision  
**Kind**: method

Returns a 2D point for the joint name you specify, relative to the input image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func pointInImage(_ jointName: VNHumanBodyPose3DObservation.JointName) throws -> VNPoint
```

## Mentions

- [Identifying 3D human body poses in images](identifying-3d-human-body-poses-in-images.md)

#### Return Value

A projection of the 3D position onto the original 2D image in normalized, lower left origin coordinates.

## Parameters

- `jointName`: The name of the human body joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/pointinimage(_:))*