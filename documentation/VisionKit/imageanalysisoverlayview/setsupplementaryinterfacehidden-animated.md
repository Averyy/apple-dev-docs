# setSupplementaryInterfaceHidden(_:animated:)

**Framework**: VisionKit  
**Kind**: method

Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func setSupplementaryInterfaceHidden(_ hidden: Bool, animated: Bool)
```

## Parameters

- `hidden`:   to hide the supplementary   interface; otherwise,  .
- `animated`:   to animate the interface   transition; otherwise,  .

## See Also

- [var supplementaryInterfaceContentInsets: NSEdgeInsets](imageanalysisoverlayview/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: NSFont?](imageanalysisoverlayview/supplementaryinterfacefont.md)
  The font to use for the supplementary interface.
- [ImageAnalysisOverlayView.MenuTag](imageanalysisoverlayview/menutag.md)
  Tags that enable your app to manage image-analysis context menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:))*