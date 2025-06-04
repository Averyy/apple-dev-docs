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

Calling this method is not required when updating your glance. This method is intended for situations where loading your glance content involves asynchronous method calls or other potentially lengthy tasks. Calling it from your [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method before you start such operations causes WatchKit to continue displaying the glance loading screen until you call the [`endGlanceUpdates()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()) method. Even if your glance is not yet onscreen, calling this method gives you extra time to process results received from an asynchronous call.

You must balance each call to this method with a corresponding call to the [`endGlanceUpdates()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()) method. Failure to do so prevents your updated glance content from being displayed. You may nest calls to this method to mark several update points. When the [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method returns, WatchKit checks for any in-progress glance updates and displays the loading screen until you make the matching calls to the [`endGlanceUpdates()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()) method.

When your interface controller’s [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method is called, WatchKit ends any outstanding glance updates automatically.

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](addmenuitem(withimagenamed:title:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:)))
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:)))
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](presentcontroller(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:)))
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](reloadrootcontrollers(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates())*