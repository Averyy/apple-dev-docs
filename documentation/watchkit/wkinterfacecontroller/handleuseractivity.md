# handleUserActivity(_:)

**Framework**: Watchkit  
**Kind**: method

Responds to Handoff–related activity.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func handleUserActivity(_ userInfo: [AnyHashable : Any]?)
```

## Overview

Implement this method in your app’s initial interface controller and use it to respond to Handoff–related activity. If you do not implement the [`handleUserActivity(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handleuseractivity(_:)) method in your app’s extension delegate, WatchKit calls this method on your app’s initial interface controller. (If your app uses a page-based interface, WatchKit calls this method for each interface controller that is part of your initial interface.) Your implementation of this method should look at the `userInfo` dictionary and decide what actions (if any) to take. For example, an interface controller in a page-based interface might make itself the current page.

The default implementation of this method does nothing. When overriding this method, do not call `super`.

## Parameters

- `userInfo`: The dictionary containing data about the activity. When launching an app from its glance, WatchKit sets this parameter to the dictionary that the glance passed to the   method.

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](addmenuitem(withimagenamed:title:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:)))
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
- [func beginGlanceUpdates()](beginglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates()))
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
- [func presentController([(name: String, context: AnyObject)])](presentcontroller(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:)))
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](reloadrootcontrollers(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:)))
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:))*