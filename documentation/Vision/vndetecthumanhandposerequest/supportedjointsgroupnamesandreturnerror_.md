# supportedJointsGroupNamesAndReturnError:

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Retrieves the supported joint group names.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
- (NSArray<NSString *> *) supportedJointsGroupNamesAndReturnError:(NSError **) error;
```

## Parameters

- `error`: If an error occurs, an error object that describes the error; otherwise, `nil`.

## See Also

### Determining Supported Joints
- [class func supportedJointNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointName]](./supportedjointnames%28forrevision%29.md)
  Retrieves the supported joint names for a revision.
- [class func supportedJointsGroupNames(forRevision: Int) throws -> [VNHumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames%28forrevision%29.md)
  Retrieves the supported joint group names for a revision.
- [- supportedJointNamesAndReturnError:](./supportedjointnamesandreturnerror_.md)
  Retrieves the supported joint names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecthumanhandposerequest/supportedjointsgroupnamesandreturnerror:)*