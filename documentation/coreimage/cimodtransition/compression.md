# compression

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The amount of stretching applied to the mod hole pattern.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var compression: Float { get set }
```

#### Discussion

Holes in the center aren’t distorted as much as those at the edge of the image.

## See Also

- [var angle: Float](cimodtransition/angle.md)
  The angle of the mod hole pattern.
- [var center: CGPoint](cimodtransition/center.md)
  The x and y position to use as the center of the effect.
- [var radius: Float](cimodtransition/radius.md)
  The radius of the undistorted mod holes in the pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimodtransition/compression)*