# handleUserActivity(_:)

**Framework**: WatchKit  
**Kind**: method

Responds to Handoff–related activity.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func handleUserActivity(_ userInfo: [AnyHashable : Any]?)
```

#### Discussion

Implement this method in your app’s initial interface controller and use it to respond to Handoff–related activity. If you do not implement the [`handleUserActivity(_:)`](wkextensiondelegate/handleuseractivity(_:).md) method in your app’s extension delegate, WatchKit calls this method on your app’s initial interface controller. (If your app uses a page-based interface, WatchKit calls this method for each interface controller that is part of your initial interface.) Your implementation of this method should look at the `userInfo` dictionary and decide what actions (if any) to take. For example, an interface controller in a page-based interface might make itself the current page.

The default implementation of this method does nothing. When overriding this method, do not call `super`.

## Parameters

- `userInfo`: The dictionary containing data about the activity. When launching an app from its glance, WatchKit sets this parameter to the dictionary that the glance passed to the   method.

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
- [func clearAllMenuItems()](wkinterfacecontroller/clearallmenuitems.md)
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](wkinterfacecontroller/endglanceupdates.md)
  Tells the system that you finished updating your glance content.
- [func presentController([(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(_:).md)
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:).md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:))*