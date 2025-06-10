# orientationTransform(for:)

**Framework**: Core Image  
**Kind**: method

The affine transform for changing the image to the given orientation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func orientationTransform(for orientation: CGImagePropertyOrientation) -> CGAffineTransform
```

#### Discussion

Returns a [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) for the [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/ImageIO/CGImagePropertyOrientation) value to apply to the image.

## See Also

- [func oriented(CGImagePropertyOrientation) -> CIImage](ciimage/oriented(_:).md)
  Transforms the original image by a given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/orientationtransform(for:))*