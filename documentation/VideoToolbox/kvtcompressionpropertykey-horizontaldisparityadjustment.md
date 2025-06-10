# kVTCompressionPropertyKey_HorizontalDisparityAdjustment

**Framework**: Video Toolbox  
**Kind**: var

A value that indicates a relative shift of the left and right images, which changes the zero parallax plane.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let kVTCompressionPropertyKey_HorizontalDisparityAdjustment: CFString
```

#### Discussion

This property sets a value for the [`kCMFormatDescriptionExtension_HorizontalDisparityAdjustment`](https://developer.apple.com/documentation/CoreMedia/kCMFormatDescriptionExtension_HorizontalDisparityAdjustment) format description on the output samples. The value is a 32-bit integer, measured over the range of `-10000` to `10000`, that maps to a uniform range of `-1.0` to `1.0`.

This property is optional. Only specify a disparity adjustment, including 0, when you know the specific value.

## See Also

- [let kVTCompressionPropertyKey_HeroEye: CFString](kvtcompressionpropertykey_heroeye.md)
  A value that indicates which eye is the primary eye when rendering in 2D.
- [let kVTCompressionPropertyKey_StereoCameraBaseline: CFString](kvtcompressionpropertykey_stereocamerabaseline.md)
  A value that specifies the distance between centers of the lenses of the camera system.
- [let kVTCompressionPropertyKey_ProjectionKind: CFString](kvtcompressionpropertykey_projectionkind.md)
  A value that indicates the projection kind.
- [let kVTCompressionPropertyKey_ViewPackingKind: CFString](kvtcompressionpropertykey_viewpackingkind.md)
  A value that indicates the view packing kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_horizontaldisparityadjustment)*