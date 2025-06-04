# reloadRootControllers(withNames:contexts:)

**Framework**: Watchkit  
**Kind**: method

Loads the specified interface controllers and rebuilds the app’s page-based interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor class func reloadRootControllers(withNames names: [String], contexts: [Any]?)
```

## Overview

Call this method to reload the pages in your app’s page-based interface:

-  Use this method to customize the set of pages you want displayed.
-  Use it to change the active set of pages, adding or removing pages as needed.

## Parameters

- `names`: An array of   objects, each of which contains the identifier of an interface controller in your storyboard file. The order of the identifiers in the array defines the order of the corresponding interface controllers in the page-based interface.
- `contexts`: An array of objects of type  . Use this parameter to pass context objects to each of the interface controllers loaded into the page-based interface. The first object in the array is passed to the first interface controller, the second object is passed to the second interface controller, and so on.

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](addmenuitem(withimagenamed:title:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:)))
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
- [func beginGlanceUpdates()](beginglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates()))
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:)))
- [func presentController([(name: String, context: AnyObject)])](presentcontroller(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:)))
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:))*