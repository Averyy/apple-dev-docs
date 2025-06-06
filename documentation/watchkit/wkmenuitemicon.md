# WKMenuItemIcon

**Framework**: Watchkit  
**Kind**: enum

Template images that you can use for menus.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKMenuItemIcon
```

#### Overview

Use these constants with the [`addMenuItem(with:title:action:)`](wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t.md) method to configure actions for your interface controller’s menu.

## Topics

### Constants
- [WKMenuItemIcon.accept](wkmenuitemicon/accept.md)
  The icon indicating an action to accept an event or item.
- [WKMenuItemIcon.add](wkmenuitemicon/add.md)
  The icon indicating an action for adding an item.
- [WKMenuItemIcon.block](wkmenuitemicon/block.md)
  The icon indicating an action to block or prevent something from happening.
- [WKMenuItemIcon.decline](wkmenuitemicon/decline.md)
  The icon indicating an action to decline or cancel an event.
- [WKMenuItemIcon.info](wkmenuitemicon/info.md)
  The icon indicating an action to retrieve more information.
- [WKMenuItemIcon.maybe](wkmenuitemicon/maybe.md)
  The icon indicating an answer of maybe for an action.
- [WKMenuItemIcon.more](wkmenuitemicon/more.md)
  The icon indicating that more actions or options are available.
- [WKMenuItemIcon.mute](wkmenuitemicon/mute.md)
  The icon indicating an action to mute the sound.
- [WKMenuItemIcon.pause](wkmenuitemicon/pause.md)
  The icon indicating an action to pause playback.
- [WKMenuItemIcon.play](wkmenuitemicon/play.md)
  The icon indicating an action to play some content.
- [WKMenuItemIcon.repeat](wkmenuitemicon/repeat.md)
  The icon indicating that played content should repeat in a loop.
- [WKMenuItemIcon.resume](wkmenuitemicon/resume.md)
  The icon indicating an action to resume playing some content.
- [WKMenuItemIcon.share](wkmenuitemicon/share.md)
  The icon indicating an action to share content.
- [WKMenuItemIcon.shuffle](wkmenuitemicon/shuffle.md)
  The icon indicating an action to shuffle content.
- [WKMenuItemIcon.speaker](wkmenuitemicon/speaker.md)
  The icon indicating audio output.
- [WKMenuItemIcon.trash](wkmenuitemicon/trash.md)
  The icon indicating an action to delete some content.
### Initializers
- [init?(rawValue: Int)](wkmenuitemicon/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Text Response Key](text-response-key.md)
  Keys for retrieving text response information.
- [func addMenuItem(withImageNamed: String, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(withimagenamed:title:action:).md)
  Adds an action to the context menu using an existing image resource in your Watch app bundle.
- [func addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-6pb4t.md)
  Adds an action to the context menu using a system-provided icon.
- [func addMenuItem(with: UIImage, title: String, action: Selector)](wkinterfacecontroller/addmenuitem(with:title:action:)-1q2zj.md)
  Adds an action to the context menu by using an image provided by your WatchKit extension.
- [func beginGlanceUpdates()](wkinterfacecontroller/beginglanceupdates.md)
  Tells the system that you are about to start a potentially lengthy update task for your glance.
- [func clearAllMenuItems()](wkinterfacecontroller/clearallmenuitems.md)
  Removes all programmatically added actions from the context menu.
- [func endGlanceUpdates()](wkinterfacecontroller/endglanceupdates.md)
  Tells the system that you finished updating your glance content.
- [func handleUserActivity([AnyHashable : Any]?)](wkinterfacecontroller/handleuseractivity(_:).md)
  Responds to Handoff–related activity.
- [func presentController([(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(_:).md)
  Presents a page-based interface modally.
- [class func reloadRootControllers(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/reloadrootcontrollers(withnames:contexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func updateUserActivity(String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](wkinterfacecontroller/updateuseractivity(_:userinfo:webpageurl:).md)
  Registers the current user activity with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)*