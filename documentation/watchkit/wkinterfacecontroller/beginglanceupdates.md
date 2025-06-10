# beginGlanceUpdates()

**Framework**: WatchKit  
**Kind**: method

Tells the system that you are about to start a potentially lengthy update task for your glance.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func beginGlanceUpdates()
```

#### Discussion

Calling this method is not required when updating your glance. This method is intended for situations where loading your glance content involves asynchronous method calls or other potentially lengthy tasks. Calling it from your [`willActivate()`](wkinterfacecontroller/willactivate().md) method before you start such operations causes WatchKit to continue displaying the glance loading screen until you call the [`endGlanceUpdates()`](wkinterfacecontroller/endglanceupdates().md) method. Even if your glance is not yet onscreen, calling this method gives you extra time to process results received from an asynchronous call.

You must balance each call to this method with a corresponding call to the [`endGlanceUpdates()`](wkinterfacecontroller/endglanceupdates().md) method. Failure to do so prevents your updated glance content from being displayed. You may nest calls to this method to mark several update points. When the [`willActivate()`](wkinterfacecontroller/willactivate().md) method returns, WatchKit checks for any in-progress glance updates and displays the loading screen until you make the matching calls to the [`endGlanceUpdates()`](wkinterfacecontroller/endglanceupdates().md) method.

When your interface controller’s [`didDeactivate()`](wkinterfacecontroller/diddeactivate().md) method is called, WatchKit ends any outstanding glance updates automatically.

## See Also

- [Text Response Key](text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(withimagenamed:title:action:).md)
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj.md)
  Adds an action to the context menu by using an image provided by your WatchKit extension.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates())*