# minimumObjectSize

**Framework**: Vision  
**Kind**: property

The minimum radius of the tracked shape’s bounding circle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var minimumObjectSize: Float { get set }
```

## Mentions

- [Identifying Trajectories in Video](identifying-trajectories-in-video.md)

#### Discussion

Set the minimum size to filter out noise and small objects. The default value is `0`, which means to apply no filtering.

Changing this property value from frame to frame can produce erratic trajectories because objects either disappear or are added to the tracking based on this filtering.

Specify the size in normalized (0.0 to 1.0) coordinates.

## See Also

- [var targetFrameTime: CMTime](vndetecttrajectoriesrequest/targetframetime.md)
  The requested target frame time for processing trajectory detection.
- [var trajectoryLength: Int](vndetecttrajectoriesrequest/trajectorylength.md)
  The number of points to detect before calculating a trajectory.
- [var objectMinimumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var objectMaximumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var maximumObjectSize: Float](vndetecttrajectoriesrequest/maximumobjectsize.md)
  The maximum radius of the tracked shape’s bounding circle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest/minimumobjectsize)*