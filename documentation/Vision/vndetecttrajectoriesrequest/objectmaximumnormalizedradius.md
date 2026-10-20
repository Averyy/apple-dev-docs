# objectMaximumNormalizedRadius

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The maximum radius of the bounding circle of the object to track.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var objectMaximumNormalizedRadius: Float { get set }
```

```objc
@property (nonatomic, assign, readwrite) float objectMaximumNormalizedRadius;
```

## See Also

### Configuring the Request
- [var targetFrameTime: CMTime](./targetframetime.md)
  The requested target frame time for processing trajectory detection.
- [var trajectoryLength: Int](./trajectorylength.md)
  The number of points to detect before calculating a trajectory.
- [var objectMinimumNormalizedRadius: Float](./objectminimumnormalizedradius.md)
  The minimum radius of the bounding circle of the object to track.
- [var minimumObjectSize: Float](./minimumobjectsize.md)
  The minimum radius of the tracked shape’s bounding circle.
- [var maximumObjectSize: Float](./maximumobjectsize.md)
  The maximum radius of the tracked shape’s bounding circle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetecttrajectoriesrequest/objectmaximumnormalizedradius)*