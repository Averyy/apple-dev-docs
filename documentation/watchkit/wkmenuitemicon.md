# WKMenuItemIcon

**Framework**: WatchKit  
**Kind**: enum

Template images that you can use for menus.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKMenuItemIcon
```

#### Overview

Use these constants with the [`addMenuItem(with:title:action:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t) method to configure actions for your interface controller’s menu.

## Topics

### Constants
- [WKMenuItemIcon.accept](accept.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/accept))
  The icon indicating an action to accept an event or item.
- [WKMenuItemIcon.add](add.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/add))
  The icon indicating an action for adding an item.
- [WKMenuItemIcon.block](block.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/block))
  The icon indicating an action to block or prevent something from happening.
- [WKMenuItemIcon.decline](decline.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/decline))
  The icon indicating an action to decline or cancel an event.
- [WKMenuItemIcon.info](info.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/info))
  The icon indicating an action to retrieve more information.
- [WKMenuItemIcon.maybe](maybe.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/maybe))
  The icon indicating an answer of maybe for an action.
- [WKMenuItemIcon.more](more.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/more))
  The icon indicating that more actions or options are available.
- [WKMenuItemIcon.mute](mute.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/mute))
  The icon indicating an action to mute the sound.
- [WKMenuItemIcon.pause](pause.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/pause))
  The icon indicating an action to pause playback.
- [WKMenuItemIcon.play](play.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/play))
  The icon indicating an action to play some content.
- [WKMenuItemIcon.repeat](repeat.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/repeat))
  The icon indicating that played content should repeat in a loop.
- [WKMenuItemIcon.resume](resume.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/resume))
  The icon indicating an action to resume playing some content.
- [WKMenuItemIcon.share](share.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/share))
  The icon indicating an action to share content.
- [WKMenuItemIcon.shuffle](shuffle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/shuffle))
  The icon indicating an action to shuffle content.
- [WKMenuItemIcon.speaker](speaker.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/speaker))
  The icon indicating audio output.
- [WKMenuItemIcon.trash](trash.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/trash))
  The icon indicating an action to delete some content.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

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
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](updateuseractivity(_:userinfo:webpageurl:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:)))
  Registers the current user activity with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)*