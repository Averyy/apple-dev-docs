# presentController(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Presents a page-based interface modally.

**Availability**:
- watchOS

> **Deprecated**: Use [`presentController(withNamesAndContexts:)`](./presentcontroller%28withnamesandcontexts%29.md) instead.

## Declaration

```swift
@MainActor
@nonobjc @preconcurrency final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)])
```

#### Discussion

After calling this method, WatchKit loads and initializes the new interface controllers and animates them into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely cover the previous interface. WatchKit displays the first interface controller in the `names` array initially. The user can navigate to the other interfaces by swiping horizontally.

The title of the modal interface is set to the string Cancel unless the presented interface controller explicitly changes it using the [`setTitle(_:)`](./settitle%28_%29.md) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](./dismiss%28%29.md) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `namesAndContexts`: An array of tuples. Each tuple must contain the following named elements:

  - **name**: The name of the interface controller you want to display. In your storyboard, the name of an interface controller is stored in the object’s Identifier property, which is located in the attributes inspector. This element must not be `nil`.
  - **context**: An object to pass to the new interface controller. Use the object in this parameter to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may specify `nil` for this element if you want but doing so is not recommended.

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
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](./reloadrootcontrollers%28withnames,contexts%29.md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](./updateuseractivity%28_,userinfo,webpageurl%29.md)
  Registers the current user activity with the system.
- [enum WKMenuItemIcon](../wkmenuitemicon.md)
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:))*