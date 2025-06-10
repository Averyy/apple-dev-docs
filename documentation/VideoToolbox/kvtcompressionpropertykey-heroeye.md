# kVTCompressionPropertyKey_HeroEye

**Framework**: Video Toolbox  
**Kind**: var

A value that indicates which eye is the primary eye when rendering in 2D.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_HeroEye: CFString
```

#### Discussion

This property sets a value for the [`kCMFormatDescriptionExtension_HeroEye`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_HeroEye) format description on the output samples. Supported values are [`kCMFormatDescriptionHeroEye_Left`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionHeroEye_Left) or [`kCMFormatDescriptionHeroEye_Right`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionHeroEye_Right).

## See Also

- [let kVTCompressionPropertyKey_StereoCameraBaseline: CFString](kvtcompressionpropertykey_stereocamerabaseline.md)
  A value that specifies the distance between centers of the lenses of the camera system.
- [let kVTCompressionPropertyKey_HorizontalDisparityAdjustment: CFString](kvtcompressionpropertykey_horizontaldisparityadjustment.md)
  A value that indicates a relative shift of the left and right images, which changes the zero parallax plane.
- [let kVTCompressionPropertyKey_ProjectionKind: CFString](kvtcompressionpropertykey_projectionkind.md)
  A value that indicates the projection kind.
- [let kVTCompressionPropertyKey_ViewPackingKind: CFString](kvtcompressionpropertykey_viewpackingkind.md)
  A value that indicates the view packing kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_heroeye)*