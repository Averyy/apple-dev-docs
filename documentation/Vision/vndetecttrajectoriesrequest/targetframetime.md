# targetFrameTime

**Framework**: Vision  
**Kind**: property

The requested target frame time for processing trajectory detection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var targetFrameTime: CMTime { get set }
```

#### Discussion

Use this property value for real-time processing of frames, which requires execution within a specific amount of time. The request evaluates from frame-to-frame. If processing takes longer than the targeted time for the current frame, it attempts to decrease the overall time by reducing the accuracy (down to a set minimum) for the next frame. If a frame takes less time than the targeted time, the request increases the accuracy (up to a set maximum) of the next frame.

The default value is [`indefinite`](https://developer.apple.com/documentation/CoreMedia/CMTime/indefinite), which indicates that accuracy stays at the predefined maximum.

## See Also

- [var trajectoryLength: Int](vndetecttrajectoriesrequest/trajectorylength.md)
  The number of points to detect before calculating a trajectory.
- [var objectMinimumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var objectMaximumNormalizedRadius: Float](vndetecttrajectoriesrequest/objectmaximumnormalizedradius.md)
  The maximum radius of the bounding circle of the object to track.
- [var minimumObjectSize: Float](vndetecttrajectoriesrequest/minimumobjectsize.md)
  The minimum radius of the tracked shape’s bounding circle.
- [var maximumObjectSize: Float](vndetecttrajectoriesrequest/maximumobjectsize.md)
  The maximum radius of the tracked shape’s bounding circle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest/targetframetime)*