# addMenuItem(withImageNamed:title:action:)

**Framework**: Watchkit  
**Kind**: method

Adds an action to the context menu using an existing image resource in your Watch app bundle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func addMenuItem(withImageNamed imageName: String, title: String, action: Selector)
```

## Overview

Use this method to append an action to the interface controller’s context menu. If the menu already has four items, additional items are ignored.

## Parameters

- `imageName`: The name of the image to be loaded from your Watch app’s bundle. Include the filename extension in the name. This parameter must not be  .
- `title`: The title string to be displayed underneath the image. Title strings should be reasonably short. Any text that cannot be displayed is truncated. This parameter must not be   or an empty string.
- `action`: The action method to be called when the action is tapped. The method must be defined on the current interface controller object. This parameter must not be  .

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
- [func beginGlanceUpdates()](beginglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates()))
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:)))
- [func presentController([(name: String, context: AnyObject)])](presentcontroller(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:)))
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](reloadrootcontrollers(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:)))
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:))*