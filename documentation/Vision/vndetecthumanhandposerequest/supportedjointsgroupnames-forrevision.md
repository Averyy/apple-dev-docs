# supportedJointsGroupNames(forRevision:)

**Framework**: Vision  
**Kind**: method

Retrieves the supported joint group names for a revision.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func supportedJointsGroupNames(forRevision revision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]
```

#### Return Value

The array of joint group name objects for the revision.

## Parameters

- `revision`: The hand pose request revision.

## See Also

- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames(forrevision:).md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](vndetecthumanhandposerequest/supportedjointsgroupnames.md)
  Retrieves the supported joint group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointsgroupnames(forrevision:))*