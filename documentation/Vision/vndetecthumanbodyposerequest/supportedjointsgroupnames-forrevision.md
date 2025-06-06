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
class func supportedJointsGroupNames(forRevision revision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]
```

#### Return Value

The array of joint group name objects for the revision.

## Parameters

- `revision`: The body pose request revision.

## See Also

- [var supportedJointNames: [VNHumanBodyPoseObservation.JointName]](vndetecthumanbodyposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointName]](vndetecthumanbodyposerequest/supportedjointnames(forrevision:).md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](vndetecthumanbodyposerequest/supportedjointsgroupnames.md)
  Retrieves the supported joint group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/supportedjointsgroupnames(forrevision:))*