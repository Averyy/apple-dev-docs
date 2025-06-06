# kVTCompressionPropertyKey_ViewPackingKind

**Framework**: Videotoolbox  
**Kind**: var

A value that indicates the view packing kind.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let kVTCompressionPropertyKey_ViewPackingKind: CFString
```

#### Discussion

The value will be set on the format description (`kCMFormatDescriptionExtension_ViewPackingKind`) for output samples and may affect the decoded frame presentation.

## See Also

- [let kVTCompressionPropertyKey_HeroEye: CFString](kvtcompressionpropertykey_heroeye.md)
  A value that indicates which eye is the primary eye when rendering in 2D.
- [let kVTCompressionPropertyKey_StereoCameraBaseline: CFString](kvtcompressionpropertykey_stereocamerabaseline.md)
  A value that specifies the distance between centers of the lenses of the camera system.
- [let kVTCompressionPropertyKey_HorizontalDisparityAdjustment: CFString](kvtcompressionpropertykey_horizontaldisparityadjustment.md)
  A value that indicates a relative shift of the left and right images, which changes the zero parallax plane.
- [let kVTCompressionPropertyKey_ProjectionKind: CFString](kvtcompressionpropertykey_projectionkind.md)
  A value that indicates the projection kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_viewpackingkind)*