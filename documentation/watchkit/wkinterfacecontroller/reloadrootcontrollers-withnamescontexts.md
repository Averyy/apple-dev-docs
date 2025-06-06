# reloadRootControllers(withNames:contexts:)

**Framework**: Watchkit  
**Kind**: method

Loads the specified interface controllers and rebuilds the app’s page-based interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
class func reloadRootControllers(withNames names: [String], contexts: [Any]?)
```

#### Discussion

Call this method to reload the pages in your app’s page-based interface:

-  Use this method to customize the set of pages you want displayed.
-  Use it to change the active set of pages, adding or removing pages as needed.

## Parameters

- `names`: An array of   objects, each of which contains the identifier of an interface controller in your storyboard file. The order of the identifiers in the array defines the order of the corresponding interface controllers in the page-based interface.
- `contexts`: An array of objects of type  . Use this parameter to pass context objects to each of the interface controllers loaded into the page-based interface. The first object in the array is passed to the first interface controller, the second object is passed to the second interface controller, and so on.

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
- [func handleUserActivity([AnyHashable : Any]?)](wkinterfacecontroller/handleuseractivity(_:).md)
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(_:).md)
  Presents a page-based interface modally.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:).md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:))*