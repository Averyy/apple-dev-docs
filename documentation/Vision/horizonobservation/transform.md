# transform

**Framework**: Vision  
**Kind**: property

The transform to apply to the detected horizon.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let transform: CGAffineTransform
```

#### Discussion

Apply the transform’s inverse to orient the image in an upright position and make the detected horizon level.

## See Also

- [func transform(for: CGSize) -> CGAffineTransform](horizonobservation/transform(for:).md)
  Creates an affine transform for the specified image width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/horizonobservation/transform)*