# supportedJointNames(forRevision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Retrieves the supported joint names for a revision.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func supportedJointNames(forRevision revision: Int) throws -> [VNHumanHandPoseObservation.JointName]
```

```objc
+ (NSArray<NSString *> *) supportedJointNamesForRevision:(NSUInteger) revision error:(NSError **) error;
```

#### Return Value

The array of joint name objects for the specified revision.

## Parameters

- `revision`: The hand pose request revision.

## See Also

### Determining Supported Joints
- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](./supportedjointnames.md)
  Retrieves the supported joint names.
- [var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointnames(forrevision:))*