# parentJointName(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the parent joint of the joint name you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func parentJointName(_ jointName: VNHumanBodyPose3DObservation.JointName) -> VNHumanBodyPose3DObservation.JointName?
```

```objc
- (VNHumanBodyPose3DObservationJointName) parentJointNameForJointName:(VNHumanBodyPose3DObservationJointName) jointName;
```

## Return Value

The name of the parent joint.

## Parameters

- `jointName`: The name of the body joint to return the parent of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhumanbodypose3dobservation/parentjointname(_:))*