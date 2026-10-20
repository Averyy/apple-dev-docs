# maximumHandCount

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum number of hands to detect in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var maximumHandCount: Int
```

#### Discussion

The request orders detected hands by relative size, with only the largest ones having key points determined.

The default value is `2`.

## See Also

### Configuring a request
- [var supportedJointNames: [HumanHandPoseObservation.JointName]](./supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanHandPoseObservation.JointsGroupName]](./supportedjointsgroupnames.md)
  The joint group names the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanhandposerequest/maximumhandcount)*