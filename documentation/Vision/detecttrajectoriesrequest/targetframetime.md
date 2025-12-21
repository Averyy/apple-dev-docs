# targetFrameTime

**Framework**: Vision  
**Kind**: property

The requested target frame time for processing trajectory detection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final var targetFrameTime: CMTime { get set }
```

#### Discussion

Use this property value for real-time processing of frames, which requires execution within a specific amount of time. The request evaluates from frame to frame. If processing takes longer than the targeted time for the current frame, it attempts to decrease the overall time by reducing the accuracy (down to a set minimum) for the next frame. If a frame takes less time than the targeted time, the request increases the accuracy (up to a set maximum) of the next frame.

The default value is indefinite, which indicates that accuracy stays at the predefined maximum.

## See Also

- [var objectMaximumNormalizedRadius: Float](detecttrajectoriesrequest/objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var objectMinimumNormalizedRadius: Float](detecttrajectoriesrequest/objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [let trajectoryLength: Int](detecttrajectoriesrequest/trajectorylength.md)
  The number of points to detect before calculating a trajectory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detecttrajectoriesrequest/targetframetime)*