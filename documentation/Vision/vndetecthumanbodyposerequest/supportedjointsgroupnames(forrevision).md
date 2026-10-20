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
class func supportedJointsGroupNames(forRevision revision: Int) throws -> [VNHumanBodyPoseObservation.JointsGroupName]
```

```objc
+ (NSArray<NSString *> *) supportedJointsGroupNamesForRevision:(NSUInteger) revision error:(NSError **) error;
```

#### Return Value

The array of joint group name objects for the revision.

## Parameters

- `revision`: The body pose request revision.

## See Also

### Determining Supported Joints
- [var supportedJointNames: [VNHumanBodyPoseObservation.JointName]](./supportedjointnames.md)
  Retrieves the supported joint names.
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanBodyPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [var supportedJointsGroupNames: [VNHumanBodyPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  Retrieves the supported joint group names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanbodyposerequest/supportedjointsgroupnames(forrevision:))*