# contentView(for:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Provides the view that contains the image.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func contentView(for overlayView: ImageAnalysisOverlayView) -> NSView?
```

#### Return Value

The view that contains the image.

#### Discussion

The default value is `nil`.

## Parameters

- `overlayView`: The associated overlay view for the content view.

## See Also

- [func contentsRect(for: ImageAnalysisOverlayView) -> CGRect](imageanalysisoverlayviewdelegate/contentsrect(for:).md)
  Returns the rectangle, in unit coordinate space, that contains the image within the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/contentview(for:))*