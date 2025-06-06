# supportedJointNames(forRevision:)

**Framework**: Vision  
**Kind**: method

Retrieves the supported joint names for a revision.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func supportedJointNames(forRevision revision: Int) throws -> [VNHumanBodyPoseObservation.JointName]
```

#### Return Value

The array of joint name objects for the specified revision.

## Parameters

- `revision`: The body pose request revision.

## See Also

- [var supportedJointNames: [VNHumanBodyPoseObservation.JointName]](vndetecthumanbodyposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vndetecthumanbodyposerequest/supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]](vndetecthumanbodyposerequest/supportedjointsgroupnames(forrevision:).md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/supportedjointnames(forrevision:))*