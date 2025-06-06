# oriented(_:)

**Framework**: Core Image  
**Kind**: instm

Transforms the original image by a given [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation) and returns the result.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func oriented(_ orientation: CGImagePropertyOrientation) -> CIImage
```

#### Discussion

Returns a new image representing the original image transformed for the given [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation).

## See Also

- [func orientationTransform(for: CGImagePropertyOrientation) -> CGAffineTransform](ciimage/2919726-orientationtransform.md)
  The affine transform for changing the image to the given orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage/2919727-oriented)*