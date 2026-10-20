# setSupplementaryInterfaceHidden(_:animated:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final func setSupplementaryInterfaceHidden(_ hidden: Bool, animated: Bool)
```

## Parameters

- `hidden`: `true` to hide the supplementary interface; otherwise, `false`.
- `animated`: `true` to animate the interface transition; otherwise, `false`.

## See Also

### Customizing the interface
- [var supplementaryInterfaceContentInsets: NSEdgeInsets](./supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: NSFont?](./supplementaryinterfacefont.md)
  The font to use for the supplementary interface.
- [ImageAnalysisOverlayView.MenuTag](./menutag.md)
  Tags that enable your app to manage image-analysis context menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:))*