# supplementaryInterfaceFont

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

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

### Customizing the interface
- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](./setsupplementaryinterfacehidden%28_,animated%29.md)
  Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: NSEdgeInsets](./supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [ImageAnalysisOverlayView.MenuTag](./menutag.md)
  Tags that enable your app to manage image-analysis context menu items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/supplementaryinterfacefont)*