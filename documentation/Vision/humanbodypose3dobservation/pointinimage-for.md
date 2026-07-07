# pointInImage(for:)

**Framework**: Vision  
**Kind**: method

Returns a 2D point for the joint name you specify, relative to the input image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func pointInImage(for jointName: HumanBodyPose3DObservation.JointName) -> NormalizedPoint
```

#### Return Value

A projection of the 3D position onto the original 2D image in normalized, lower left origin coordinates.

## Parameters

- `jointName`: The name of the human body joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/humanbodypose3dobservation/pointinimage(for:))*