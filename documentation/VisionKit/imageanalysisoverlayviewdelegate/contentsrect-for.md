# contentsRect(for:)

**Framework**: VisionKit  
**Kind**: method  
**Required**: Yes

Returns the rectangle, in unit coordinate space, that contains the image within the view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func contentsRect(for overlayView: ImageAnalysisOverlayView) -> CGRect
```

#### Return Value

The rectangle of the image within the view, in unit coordinates. The default return value is the unit rectangle `[0.0, 0.0, 1.0, 1.0]`, which represents the whole view contents.

#### Discussion

Implement this method if the [`trackingImageView`](imageanalysisoverlayview/trackingimageview.md) type isn’t [`NSImageView`](https://developer.apple.com/documentation/AppKit/NSImageView).

## Parameters

- `overlayView`: The associated overlay view for the contents rectangle.

## See Also

- [func contentView(for: ImageAnalysisOverlayView) -> NSView?](imageanalysisoverlayviewdelegate/contentview(for:).md)
  Provides the view that contains the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/contentsrect(for:))*