# reloadRootControllers(withNames:contexts:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Type Method

Loads the specified interface controllers and rebuilds the app’s page-based interface.

**Availability**:
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use [`reloadRootPageControllers(withNames:contexts:orientation:pageIndex:)`](./reloadrootpagecontrollers%28withnames,contexts,orientation,pageindex%29.md) instead.

## Declaration

```swift
class func reloadRootControllers(withNames names: [String], contexts: [Any]?)
```

```objc
+ (void) reloadRootControllersWithNames:(NSArray<NSString *> *) names contexts:(NSArray *) contexts;
```

## Discussion

Call this method to reload the pages in your app’s page-based interface:

- **At launch time.** Use this method to customize the set of pages you want displayed.
- **At runtime.** Use it to change the active set of pages, adding or removing pages as needed.

## Parameters

- `names`: An array of [`NSString`](../../Foundation/nsstring.md) objects, each of which contains the identifier of an interface controller in your storyboard file. The order of the identifiers in the array defines the order of the corresponding interface controllers in the page-based interface.
- `contexts`: An array of objects of type `id`. Use this parameter to pass context objects to each of the interface controllers loaded into the page-based interface. The first object in the array is passed to the first interface controller, the second object is passed to the second interface controller, and so on.

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
- [func clearAllMenuItems()](./clearallmenuitems%28%29.md)
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](./endglanceupdates%28%29.md)
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](./handleuseractivity%28_%29.md)
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](./presentcontroller%28_%29.md)
  Presents a page-based interface modally.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](./updateuseractivity%28_,userinfo,webpageurl%29.md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](../wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:))*