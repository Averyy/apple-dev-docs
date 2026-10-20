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
var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName] { get throws }
```

## See Also

### Determining Supported Joints
- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](./supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointsgroupnames)*