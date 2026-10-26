# overlayView(_:menu:willHighlight:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default, blank implementation for when an overlay view menu highlights.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, menu: NSMenu, willHighlight menuItem: NSMenuItem?)
```

## Parameters

- `overlayView`: The interaction object for the Live Text interface.
- `menu`: The menu that contains the item to be highlighted.
- `menuItem`: The menu item to be highlighted, or nil if transitioning to no highlighted items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:menu:willhighlight:)-k1tr)*