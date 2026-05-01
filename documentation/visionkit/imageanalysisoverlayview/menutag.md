# ImageAnalysisOverlayView.MenuTag

**Framework**: VisionKit  
**Kind**: struct

Tags that enable your app to manage image-analysis context menu items.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MenuTag
```

#### Overview

Manage app context menu items by implementing the [`ImageAnalysisOverlayViewDelegate`](imageanalysisoverlayviewdelegate.md) menu-related callbacks and referencing the menu item instances using tags from this enumeration. For example, see [`overlayView(_:updatedMenuFor:for:at:)`](imageanalysisoverlayviewdelegate/overlayview(_:updatedmenufor:for:at:).md).

## Topics

### Manage Framework-provided menu items
- [static let copyImage: Int](imageanalysisoverlayview/menutag/copyimage.md)
  An index for the copy-image menu item.
- [static let shareImage: Int](imageanalysisoverlayview/menutag/shareimage.md)
  An index for the share-image menu item.
- [static let copySubject: Int](imageanalysisoverlayview/menutag/copysubject.md)
  An index for the copy-subject menu item.
- [static let shareSubject: Int](imageanalysisoverlayview/menutag/sharesubject.md)
  An index for the share-subject menu item.
- [static let lookupItem: Int](imageanalysisoverlayview/menutag/lookupitem.md)
  An index for the Visual Look Up menu item.
### Create app-defined menu items
- [static let recommendedAppItems: Int](imageanalysisoverlayview/menutag/recommendedappitems.md)
  An index for app-provided menu items.

## See Also

- [func setSupplementaryInterfaceHidden(Bool, animated: Bool)](imageanalysisoverlayview/setsupplementaryinterfacehidden(_:animated:).md)
  Hides or shows supplementary interface objects, such as the Live Text button and the interface for Quick Actions, depending on the item type.
- [var supplementaryInterfaceContentInsets: NSEdgeInsets](imageanalysisoverlayview/supplementaryinterfacecontentinsets.md)
  The distances the edges of content are inset from the supplementary interface.
- [var supplementaryInterfaceFont: NSFont?](imageanalysisoverlayview/supplementaryinterfacefont.md)
  The font to use for the supplementary interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview/menutag)*