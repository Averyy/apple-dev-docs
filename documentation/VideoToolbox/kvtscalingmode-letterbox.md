# kVTScalingMode_Letterbox

**Framework**: Video Toolbox  
**Kind**: var

The source image buffer’s clean aperture is scaled to a rectangle fitted inside the  destination clean aperture that preserves the source picture aspect ratio.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
let kVTScalingMode_Letterbox: CFString
```

#### Discussion

The remainder of the destination image buffer is filled with black. If a destination pixel aspect ratio is not set, the source image’s pixel aspect ratio is used. The pixel aspect ratio used is set on the destination image buffer.

## See Also

- [let kVTScalingMode_Normal: CFString](kvtscalingmode_normal.md)
  The full width and height of the source image buffer is stretched to the full width and height of the destination image buffer.
- [let kVTScalingMode_CropSourceToCleanAperture: CFString](kvtscalingmode_cropsourcetocleanaperture.md)
  The source image buffer’s clean aperture is scaled to the destination clean aperture.
- [let kVTScalingMode_Trim: CFString](kvtscalingmode_trim.md)
  The source image buffer’s clean aperture is scaled to a rectangle that completely fills the destination clean aperture and preserves the source picture aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvtscalingmode_letterbox)*