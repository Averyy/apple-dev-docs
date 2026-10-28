# minimumObjectSize

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The minimum radius of the tracked shape’s bounding circle.

**Availability**:
- iOS 14.0+ - Deprecated in 14.0
- iPadOS 14.0+ - Deprecated in 14.0
- Mac Catalyst 14.0+ - Deprecated in 14.0
- macOS 11.0+ - Deprecated in 11.0
- tvOS 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`objectMinimumNormalizedRadius`](./objectminimumnormalizedradius.md) instead.

## Declaration

```swift
var minimumObjectSize: Float { get set }
```

```objc
@property (nonatomic, assign, readwrite) float minimumObjectSize;
```

## Mentions

- [Identifying Trajectories in Video](../identifying-trajectories-in-video.md)

## Discussion

Set the minimum size to filter out noise and small objects. The default value is `0`, which means to apply no filtering.

Changing this property value from frame to frame can produce erratic trajectories because objects either disappear or are added to the tracking based on this filtering.

Specify the size in normalized (0.0 to 1.0) coordinates.

## See Also

### Configuring the Request
- [var targetFrameTime: CMTime](./targetframetime.md)
  The requested target frame time for processing trajectory detection.
- [var trajectoryLength: Int](./trajectorylength.md)
  The number of points to detect before calculating a trajectory.
- [var objectMinimumNormalizedRadius: Float](./objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var objectMaximumNormalizedRadius: Float](./objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var maximumObjectSize: Float](./maximumobjectsize.md)
  The maximum radius of the tracked shape’s bounding circle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest/minimumobjectsize)*