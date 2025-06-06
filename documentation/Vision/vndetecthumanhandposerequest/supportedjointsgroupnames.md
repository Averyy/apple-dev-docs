# supportedJointsGroupNames

**Framework**: Vision  
**Kind**: property

Retrieves the supported joint group names.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName] { get throws }
```

## See Also

- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](vndetecthumanhandposerequest/supportedjointnames(forrevision:).md)
  Retrieves the supported joint names for a revision.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]](vndetecthumanhandposerequest/supportedjointsgroupnames(forrevision:).md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointsgroupnames)*