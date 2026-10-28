# detectsHands

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that detects hands of the body in the results, if they’re visible.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var detectsHands: Bool
```

## Discussion

The default value is `true,` and requires [`DetectHumanBodyPoseRequest.Revision.revision2`](./revision-swift.enum/revision2.md).

## See Also

### Configuring a request
- [var supportedJointNames: [HumanBodyPoseObservation.JointName]](./supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanBodyPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  The joint group names the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest/detectshands)*