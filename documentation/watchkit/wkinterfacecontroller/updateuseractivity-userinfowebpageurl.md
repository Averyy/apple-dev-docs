# updateUserActivity(_:userInfo:webpageURL:)

**Framework**: WatchKit  
**Kind**: method

Registers the current user activity with the system.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func updateUserActivity(_ type: String, userInfo: [AnyHashable : Any]? = nil, webpageURL: URL?)
```

#### Discussion

Use this method to publish your app’s current activity so that it can be handled as needed. When calling this method, you must specify a value for the `userInfo` parameter, the `webpageURL` parameter, or both. Call this method in the following situations:

- In your glance interface controller, call this method and provide a `userInfo` dictionary with information about what the glance displays. If the user taps your glance, that contextual information passes to your app so it can configure its interface.
- Call this method to register the current activity with Handoff. The system delivers the information to the user’s iPhone, which can propagate the Handoff information to the user’s other devices. For more information about supporting Handoff, see [`Handoff Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Handoff/HandoffFundamentals/HandoffFundamentals.html#//apple_ref/doc/uid/TP40014338).

Call this method at any time during the execution of your interface controller’s code. The system takes the information you provide and stores it for delivery to the appropriate target.

## Parameters

- `type`: The type of activity to be continued. The value is a developer-defined string in reverse-DNS format by convention, for example,  . This parameter must not be   or an empty string.
- `userInfo`: A dictionary containing app-specific state information needed to continue an activity on another device. Keys and values in the dictionary must be of the following types:  ,  ,  ,  ,  ,  ,  , or  .
- `webpageURL`: A URL containing the web page to load in a browser to continue the activity. The scheme of the URL must be   or  . Any other scheme throws an exception.

## See Also

- [Text Response Key](text-response-key.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/text-response-key))
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](addmenuitem(withimagenamed:title:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(withimagenamed:title:action:)))
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](addmenuitem(with:title:action:)-6pb4t.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t))
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](addmenuitem(with:title:action:)-1q2zj.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj))
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func beginGlanceUpdates()](beginglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/beginglanceupdates()))
  Tells the system that you are about to start a potentially lengthy update task for your glance.
- [func clearAllMenuItems()](clearallmenuitems().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/clearallmenuitems()))
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](endglanceupdates().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/endglanceupdates()))
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](handleuseractivity(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/handleuseractivity(_:)))
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](presentcontroller(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(_:)))
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](reloadrootcontrollers(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))
  Template images that you can use for menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:))*