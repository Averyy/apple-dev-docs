# supportedJointNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

Retrieves the supported joint names.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var supportedJointNames: [VNHumanBodyPoseObservation.JointName] { get throws }
```

## See Also

### Determining Supported Joints
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]](./supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/supportedjointnames)*