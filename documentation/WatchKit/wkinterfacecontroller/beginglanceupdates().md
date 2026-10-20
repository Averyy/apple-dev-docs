# beginGlanceUpdates()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the system that you are about to start a potentially lengthy update task for your glance.

**Availability**:
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: watchOS no longer supports glances.

## Declaration

```swift
func beginGlanceUpdates()
```

```objc
- (void) beginGlanceUpdates;
```

#### Discussion

Calling this method is not required when updating your glance. This method is intended for situations where loading your glance content involves asynchronous method calls or other potentially lengthy tasks. Calling it from your [`willActivate()`](./willactivate%28%29.md) method before you start such operations causes WatchKit to continue displaying the glance loading screen until you call the [`endGlanceUpdates()`](./endglanceupdates%28%29.md) method. Even if your glance is not yet onscreen, calling this method gives you extra time to process results received from an asynchronous call.

You must balance each call to this method with a corresponding call to the [`endGlanceUpdates()`](./endglanceupdates%28%29.md) method. Failure to do so prevents your updated glance content from being displayed. You may nest calls to this method to mark several update points. When the [`willActivate()`](./willactivate%28%29.md) method returns, WatchKit checks for any in-progress glance updates and displays the loading screen until you make the matching calls to the [`endGlanceUpdates()`](./endglanceupdates%28%29.md) method.

When your interface controller’s [`didDeactivate()`](./diddeactivate%28%29.md) method is called, WatchKit ends any outstanding glance updates automatically.

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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates())*