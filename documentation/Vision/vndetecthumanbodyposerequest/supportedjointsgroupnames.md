# supportedJointsGroupNames

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

Retrieves the supported joint group names.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName] { get throws }
```

## See Also

### Determining Supported Joints
- [var supportedJointNames: [VNHumanBodyPoseObservation.JointName]](./supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]](./supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/supportedjointsgroupnames)*