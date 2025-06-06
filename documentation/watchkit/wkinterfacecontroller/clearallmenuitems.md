# clearAllMenuItems()

**Framework**: Watchkit  
**Kind**: method

Removes all programmatically added actions from the context menu.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func clearAllMenuItems()
```

#### Discussion

Use this method to remove all menu items that you added using the [`addMenuItem(with:title:action:)`](wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj.md) or [`addMenuItem(withImageNamed:title:action:)`](wkinterfacecontroller/addmenuitem(withimagenamed:title:action:).md) method. This method does not remove menu items that you configured in the storyboard file.

## See Also

- [Text Response Key](text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(withimagenamed:title:action:).md)
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj.md)
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func beginGlanceUpdates()](wkinterfacecontroller/beginglanceupdates.md)
  Tells the system that you are about to start a potentially lengthy update task for your glance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems())*