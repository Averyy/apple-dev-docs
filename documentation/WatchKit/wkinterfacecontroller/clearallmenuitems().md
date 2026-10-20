# clearAllMenuItems()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes all programmatically added actions from the context menu.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Elevate important items out of such menus and into the relevant screen or a settings screen.

## Declaration

```swift
func clearAllMenuItems()
```

```objc
- (void) clearAllMenuItems;
```

#### Discussion

Use this method to remove all menu items that you added using the [`addMenuItem(with:title:action:)`](./addmenuitem%28with,title,action%29-1q2zj.md) or [`addMenuItem(withImageNamed:title:action:)`](./addmenuitem%28withimagenamed,title,action%29.md) method. This method does not remove menu items that you configured in the storyboard file.

## See Also

### Deprecated symbols
- [Text Response Key](../text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](./addmenuitem%28withimagenamed,title,action%29.md)
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](./addmenuitem%28with,title,action%29-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](./addmenuitem%28with,title,action%29-1q2zj.md)
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func beginGlanceUpdates()](./beginglanceupdates%28%29.md)
  Tells the system that you are about to start a potentially lengthy update task for your glance.
- [func endGlanceUpdates()](./endglanceupdates%28%29.md)
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](./handleuseractivity%28_%29.md)
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](./presentcontroller%28_%29.md)
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](./reloadrootcontrollers%28withnames,contexts%29.md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](./updateuseractivity%28_,userinfo,webpageurl%29.md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](../wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems())*