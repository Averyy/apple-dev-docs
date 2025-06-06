# supplementaryInterfaceFont

**Framework**: Visionkit  
**Kind**: property

The font to use for the supplementary interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
final var supplementaryInterfaceFont: NSFont? { get set }
```

#### Discussion

The interaction also uses the font weight for image symbols, but ignores the point size to keep button sizes consistent.

## See Also

- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:).md)
  Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: NSEdgeInsets](imageanalysisoverlayview/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [ImageAnalysisOverlayView.MenuTag](imageanalysisoverlayview/menutag.md)
  Tags that enable your app to manage image-analysis context menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/supplementaryinterfacefont)*