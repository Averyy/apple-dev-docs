# supportedJointsGroupNames(forRevision:)

**Framework**: Vision  
**Kind**: method  
**Role**: Type Method

Retrieves the supported joint group names for a revision.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class func supportedJointsGroupNames(forRevision revision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]
```

```objc
+ (NSArray<NSString *> *) supportedJointsGroupNamesForRevision:(NSUInteger) revision error:(NSError **) error;
```

#### Return Value

The array of joint group name objects for the revision.

## Parameters

- `revision`: The hand pose request revision.

## See Also

### Determining Supported Joints
- [var supportedJointNames: [VNHumanHandPoseObservation.JointName]](./supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  Retrieves the supported joint group names.
- [- supportedJointNamesAndReturnError:](./supportedjointnamesandreturnerror_.md)
  Retrieves the supported joint names.
- [- supportedJointsGroupNamesAndReturnError:](./supportedjointsgroupnamesandreturnerror_.md)
  Retrieves the supported joint group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointsgroupnames(forrevision:))*