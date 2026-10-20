# contentView(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
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

## Default Implementations

### ImageAnalysisOverlayViewDelegate Implementations
- [func contentView(for: ImageAnalysisOverlayView) -> NSView?](./contentview%28for%29-khdt.md)
  A default implementation that returns a `nil` reference.

## See Also

### Providing interface details
- [func contentsRect(for: ImageAnalysisOverlayView) -> CGRect](./contentsrect%28for%29.md)
  Returns the rectangle, in unit coordinate space, that contains the image within the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/contentview(for:))*