# overlayView(_:updatedMenuFor:for:at:)

**Framework**: Visionkit  
**Kind**: method  
**Required**: Yes

Notifies your app before the framework presents a context menu.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
func overlayView(_ overlayView: ImageAnalysisOverlayView, updatedMenuFor menu: NSMenu, for event: NSEvent, at point: CGPoint) -> NSMenu
```

#### Discussion

This callback enables your app to add custom context menu items or manage the framework-provided content menu items. For example, the following implementation changes the title of the framework-provided `copySubject` menu item from “Copy” to “Copy and remove background”.

```swift
func overlayView(_ overlayView: ImageAnalysisOverlayView, updateMenu menu: NSMenu, forEvent: NSEvent, atPoint point: CGPoint) -> NSMenu {

    let copySubjectItem = menu.item(withTag:ImageAnalysisOverlayView.MenuTag.copySubject)
    copySubjectItem.title = "Copy and remove background"

    return menu
}
```

The menu items don’t persist. However, your app can alter menu items and share them across different menus within the same menu session.

To add items to a menu, access  the recommended index for insertion by using the [`recommendedAppItems`](imageanalysisoverlayview/menutag/recommendedappitems.md) menu tag, such as in the following code:

```swift
func overlayView(_ overlayView: ImageAnalysisOverlayView, updateMenu menu: NSMenu, forEvent: NSEvent, atPoint point: CGPoint) -> NSMenu {

    let item = NSMenuItem()
    let tag = ImageAnalysisOverlayView.MenuTag.recommendedAppItems
    let index = menu.indexOfItem(withTag:tag)
    menu.insertItem(item, at: index)

    return menu
}
```

> **Note**: The framework is the delegate for the returned menu item. The framework continues to support [`NSMenuDelegate`](https://developer.apple.com/documentation/AppKit/NSMenuDelegate) callbacks for VisionKit-specific menu items.

The framework is the delegate for the returned menu item. The framework continues to support [`NSMenuDelegate`](https://developer.apple.com/documentation/AppKit/NSMenuDelegate) callbacks for VisionKit-specific menu items.

## Parameters

- `overlayView`: The associated overlay view for the updated menu.
- `menu`: The menu that appears.
- `event`: The event associated with this menu.
- `point`: The original location of the event for the menu.

## See Also

- [func overlayView(ImageAnalysisOverlayView, shouldHandleKeyDownEvent: NSEvent) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldhandlekeydownevent:).md)
  Returns a Boolean value that indicates whether the overlay view consumes the given key-down event.
- [func overlayView(ImageAnalysisOverlayView, shouldShowMenuForEvent: NSEvent, atPoint: CGPoint) -> Bool](imageanalysisoverlayviewdelegate/overlayview(_:shouldshowmenuforevent:atpoint:).md)
  Provides a Boolean value that indicates whether the overlay view shows a menu for the given event.
- [func overlayView(ImageAnalysisOverlayView, menu: NSMenu, willHighlight: NSMenuItem?)](imageanalysisoverlayviewdelegate/overlayview(_:menu:willhighlight:).md)
  Notifies your app that the given menu item is highlighted.
- [func overlayView(ImageAnalysisOverlayView, willOpen: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:willopen:).md)
  Notifies your app that a given menu is opening imminently.
- [func overlayView(ImageAnalysisOverlayView, didClose: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:didclose:).md)
  Notifies your app that the given menu closed.
- [func overlayView(ImageAnalysisOverlayView, needsUpdate: NSMenu)](imageanalysisoverlayviewdelegate/overlayview(_:needsupdate:).md)
  Notifies your app that the given menu needs updating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate/overlayview(_:updatedmenufor:for:at:))*