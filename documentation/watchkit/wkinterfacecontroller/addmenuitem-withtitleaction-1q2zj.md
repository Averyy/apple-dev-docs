# addMenuItem(with:title:action:)

**Framework**: Watchkit  
**Kind**: method

Adds an action to the context menu by using an image provided by your WatchKit extension.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func addMenuItem(with image: UIImage, title: String, action: Selector)
```

#### Discussion

Use this method to append an action to the interface controller’s context menu. If the menu already has four items, additional items are ignored.

## Parameters

- `image`: The template image to be used for the action. Only the alpha channel of the image is used. This parameter must not be  . For information about the dimensions for menu images, see  .
- `title`: The title string to be displayed underneath the image. Title strings should be reasonably short. Any text that cannot be displayed is truncated. This parameter must not be   or an empty string.
- `action`: The action method to be called when the action is tapped. The method must be defined on the current interface controller object. This parameter must not be  .

## See Also

- [Text Response Key](text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(withimagenamed:title:action:).md)
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func beginGlanceUpdates()](wkinterfacecontroller/beginglanceupdates.md)
  Tells the system that you are about to start a potentially lengthy update task for your glance.
- [func clearAllMenuItems()](wkinterfacecontroller/clearallmenuitems.md)
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](wkinterfacecontroller/endglanceupdates.md)
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](wkinterfacecontroller/handleuseractivity(_:).md)
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(_:).md)
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:).md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj)*