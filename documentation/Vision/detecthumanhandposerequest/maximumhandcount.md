# maximumHandCount

**Framework**: Vision  
**Kind**: property

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

- [var supportedJointNames: [HumanHandPoseObservation.JointName]](detecthumanhandposerequest/supportedjointnames.md)
  The joint names the request supports.
- [var supportedJointsGroupNames: [HumanHandPoseObservation.JointsGroupName]](detecthumanhandposerequest/supportedjointsgroupnames.md)
  The joint group names the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecthumanhandposerequest/maximumhandcount)*