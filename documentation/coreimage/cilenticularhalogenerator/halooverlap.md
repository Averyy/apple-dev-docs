# haloOverlap

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The separation of colors in the halo.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var haloOverlap: Float { get set }
```

#### Discussion

A value of `0` means the halo colors don’t overlap. A value of `1` means the halo colors fully overlap, creating a white halo.

## See Also

- [var center: CGPoint](cilenticularhalogenerator/center.md)
  The x and y position to use as the center of the halo.
- [var color: CIColor](cilenticularhalogenerator/color.md)
  The color of the halo.
- [var haloRadius: Float](cilenticularhalogenerator/haloradius.md)
  The radius of the halo.
- [var haloWidth: Float](cilenticularhalogenerator/halowidth.md)
  The width of the halo, from its inner radius to its outer radius.
- [var striationContrast: Float](cilenticularhalogenerator/striationcontrast.md)
  The contrast of the halo colors.
- [var striationStrength: Float](cilenticularhalogenerator/striationstrength.md)
  The intensity of the halo colors.
- [var time: Float](cilenticularhalogenerator/time.md)
  The current time of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator/halooverlap)*