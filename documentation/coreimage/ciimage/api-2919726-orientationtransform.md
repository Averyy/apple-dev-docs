# orientationTransform(for:)

**Framework**: Core Image  
**Kind**: instm

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

Returns a [`CGAffineTransform`](https://developer.apple.com/documentation/corefoundation/cgaffinetransform) for the [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation) value to apply to the image.

## See Also

- [func oriented(CGImagePropertyOrientation) -> CIImage](ciimage/2919727-oriented.md)
  Transforms the original image by a given [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation) and returns the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/2919726-orientationtransform)*