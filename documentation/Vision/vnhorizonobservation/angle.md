# angle

**Framework**: Vision  
**Kind**: property

The angle of the observed horizon.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var angle: CGFloat { get }
```

#### Discussion

Use the angle to orient the image in an upright position and make the detected horizon level.

## See Also

- [var transform: CGAffineTransform](vnhorizonobservation/transform.md)
  The transform to apply to the detected horizon.
- [func transform(forImageWidth: Int, height: Int) -> CGAffineTransform](vnhorizonobservation/transform(forimagewidth:height:).md)
  Creates an affine transform for the specified image width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhorizonobservation/angle)*