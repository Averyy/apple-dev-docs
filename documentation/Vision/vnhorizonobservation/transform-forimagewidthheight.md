# transform(forImageWidth:height:)

**Framework**: Vision  
**Kind**: method

Creates an affine transform for the specified image width and height.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func transform(forImageWidth width: Int, height: Int) -> CGAffineTransform
```

#### Return Value

An affine transform.

## Parameters

- `width`: The width of the image.
- `height`: The height of the image.

## See Also

- [var angle: CGFloat](vnhorizonobservation/angle.md)
  The angle of the observed horizon.
- [var transform: CGAffineTransform](vnhorizonobservation/transform.md)
  The transform to apply to the detected horizon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhorizonobservation/transform(forimagewidth:height:))*