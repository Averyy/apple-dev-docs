# addMenuItem(withImageNamed:title:action:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Adds an action to the context menu using an existing image resource in your Watch app bundle.

**Availability**:
- watchOS 2.0+ - Deprecated in 7.0

> **Deprecated**: Elevate important items out of such menus and into the relevant screen or a settings screen.

## Declaration

```swift
func addMenuItem(withImageNamed imageName: String, title: String, action: Selector)
```

```objc
- (void) addMenuItemWithImageNamed:(NSString *) imageName title:(NSString *) title action:(SEL) action;
```

#### Discussion

Use this method to append an action to the interface controller’s context menu. If the menu already has four items, additional items are ignored.

## Parameters

- `imageName`: The name of the image to be loaded from your Watch app’s bundle. Include the filename extension in the name. This parameter must not be `nil`.
- `title`: The title string to be displayed underneath the image. Title strings should be reasonably short. Any text that cannot be displayed is truncated. This parameter must not be `nil` or an empty string.
- `action`: The action method to be called when the action is tapped. The method must be defined on the current interface controller object. This parameter must not be `nil`.

## See Also

### Deprecated symbols
- [Text Response Key](../text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](./addmenuitem%28with,title,action%29-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](./addmenuitem%28with,title,action%29-1q2zj.md)
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func beginGlanceUpdates()](./beginglanceupdates%28%29.md)
  Tells the system that you are about to start a potentially lengthy update task for your glance.
- [func clearAllMenuItems()](./clearallmenuitems%28%29.md)
  Removes all programmatically added actions from the context menu.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:))*