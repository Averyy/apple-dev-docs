# presentController(_:)

**Framework**: Watchkit  
**Kind**: method

Presents a page-based interface modally.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Unknown ?+ - Deprecated
- watchOS ?+

## Declaration

```swift
@MainActor @nonobjc @preconcurrency final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)])
```

## Overview

After calling this method, WatchKit loads and initializes the new interface controllers and animates them into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely cover the previous interface. WatchKit displays the first interface controller in the `names` array initially. The user can navigate to the other interfaces by swiping horizontally.

The title of the modal interface is set to the string Cancel unless the presented interface controller explicitly changes it using the [`setTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:)) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `namesAndContexts`: An array of tuples. Each tuple must contain the following named elements:

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](addmenuitem(withimagenamed:title:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:)))
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
- [func beginGlanceUpdates()](beginglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates()))
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:)))
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](reloadrootcontrollers(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:)))
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:))*