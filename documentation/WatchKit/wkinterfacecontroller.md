# WKInterfaceController

**Framework**: WatchKit  
**Kind**: class

A class that provides the infrastructure for managing the interface in a watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
class WKInterfaceController
```

#### Overview

An interface controller serves the same purpose as a [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) object in a UIKit app, except that it doesn’t manage any actual views. It runs in your WatchKit extension and remotely manages the behavior associated with an interface controller in your Watch app’s storyboard file. You subclass [`WKInterfaceController`](wkinterfacecontroller.md) and use its methods to configure the elements of your storyboard scene and to respond to interactions with those elements.

Your interface controller code runs locally on the user’s Apple Watch but is separate from the interface that it manages. When you change the value of an interface object in your code, the system forwards the needed information to your Watch app, which makes the corresponding changes onscreen.

##### Initialize Your Interface Controllers

When the user interacts with your app content, the system launches your extension and creates the appropriate interface controller objects automatically. Apps use different interface controllers to manage their notification and app interfaces; WatchKit uses the information in your app’s main storyboard file to determine which interface controller to load. Notification scenes are configured specially so that the system can identify them. For your app, WatchKit loads your app’s main interface controller initially, but you may change the initial interface controller at launch time.

When creating an interface controller, WatchKit instantiates the class and calls its [`init()`](wkinterfacecontroller/init().md) method. You can use this method to initialize variables and load data; however, don’t use it to configure your user interface. The controller’s user interface elements may not be properly initialized when this method runs.

Next, the system calls the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method. If WatchKit passes a valid object to the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method, use the information in that object to customize the initialization process. Also, the controller’s user interface elements are guaranteed to be available at this point. This means that you can safely use this method to configure your user interface.

The [`willActivate()`](wkinterfacecontroller/willactivate().md) method lets you know when your interface is about to become active. Use the [`willActivate()`](wkinterfacecontroller/willactivate().md) method to perform any last minute tasks, such as checking for updates to your content; however, don’t use it for your primary initialization.

The [`willActivate()`](wkinterfacecontroller/willactivate().md) method may be called at times when your interface isn’t yet onscreen. For example, WatchKit may call the method in advance so that you have time to update your content. WatchKit calls the [`didAppear()`](wkinterfacecontroller/didappear().md) method to let you know when your interface becomes visible. Similarly, WatchKit calls the [`willDisappear()`](wkinterfacecontroller/willdisappear().md) and [`didDeactivate()`](wkinterfacecontroller/diddeactivate().md) methods when your interface moves offscreen again.

> ❗ **Important**:  An interface controller can make changes to its interface only in the [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) method, in the [`willActivate()`](wkinterfacecontroller/willactivate().md) method, and while the interface is active. Once the system calls the [`didDeactivate()`](wkinterfacecontroller/diddeactivate().md) method, it ignores any attempts to change the value of the controller’s interface objects until the system calls the interface controller’s [`willActivate()`](wkinterfacecontroller/willactivate().md) method again.

In iOS Simulator, WatchKit calls the [`didDeactivate()`](wkinterfacecontroller/diddeactivate().md) method for the current interface controller when you lock the simulator by selecting Hardware > Lock. When you subsequently unlock the simulator, WatchKit calls that interface controller’s [`willActivate()`](wkinterfacecontroller/willactivate().md) method again. You can use this capability to debug your activation and deactivation code.

##### Interface Builder Configuration Options

Xcode lets you configure information about your interface controller in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Identifier | The name of the interface controller. Use this name to specify which interface controller to push or present. |
| Title | The title string assigned to the interface controller. You can set this value programmatically using the [`setTitle(_:)`](wkinterfacecontroller/settitle(_:).md) method. |
| Is Initial Controller | A Boolean indicating whether the object is the app’s root interface controller. Only one interface controller at a time may have this option enabled. This option doesn’t apply to glance or notification interface controllers. |
| Activity Indicator On Load | A Boolean value that indicates whether the interface controller’s contents are hidden until the [`willActivate()`](wkinterfacecontroller/willactivate().md) method returns. When you enable this option, the system displays a progress indicator until the [`willActivate()`](wkinterfacecontroller/willactivate().md) method returns. You might disable this option if your interface contains mostly static information that can be displayed right away. |
| Always Bounce | A Boolean value that turns off scrolling and allows built-in controls and containers to fill content to the screen edges, regardless of the content-safe area. |
| Full Screen | A Boolean value that determines whether SpriteKit or SceneKit content can use the full screen. The system hides the status bar but displays the time in the upper-right corner with a gradient behind it, making the time clearly visible against the scene. |
| Fixed to screen edges | A Boolean value that indicates whether the contents ignore the safe area and minimum layout margins. When you enable this option, the system turns off scrolling, and allows built-in controls and containers to fill content to the screen edges. |
| Background | The background image displayed behind the scene’s content. The image specified in your storyboard scrolls with your interface controller’s content. |
| Mode | The content mode for the background image. This mode defines how the background image scales or fills the screen and behaves in the same way as the constants for the [`UIView.ContentMode`](https://developer.apple.com/documentation/UIKit/UIView/ContentMode-swift.enum) type. |
| Animate | A Boolean value indicating whether an animated background image starts running its animation automatically after being loaded. Set this option to `Yes` if you want the animation to start automatically; set it to `No` if you prefer to start the animation programmatically. |
| Color | The background color to be displayed behind the scene’s content. |
| Insets | The amount of space (in points) to insert between the edges of the interface controller and its content. Select Custom to specify different values for the top, bottom, left, and right edges. |
| Spacing | Additional spacing (in points) to include between items in the interface controller. |

##### Subclassing Notes

Subclass `WKInterfaceController` when you have a storyboard scene that requires configuration at runtime or that handles user interactions. Typically, you define a custom subclass for each unique storyboard scene that your app manages. In your subclass, define outlets for any interface objects you need to configure and define action methods for responding to interactions with the elements of your storyboard scene.

Most custom interface controllers you use in your app require a custom interface controller subclass. Even glances need an interface controller to update the glance contents. The only storyboard scene that can’t use a custom interface controller is the scene associated with a static notification interface. When implementing an interface controller for your dynamic notification interface, subclass [`WKUserNotificationInterfaceController`](wkusernotificationinterfacecontroller.md) instead.

Override any methods of the class needed to configure your interface and get it ready to display. Most interface controllers override the [`init()`](wkinterfacecontroller/init().md) and [`awake(withContext:)`](wkinterfacecontroller/awake(withcontext:).md) methods. Override any other methods that make sense based on your needs.

## Topics

### Creating the interface controller
- [init()](wkinterfacecontroller/init.md)
  Returns an initialized interface controller object.
- [func awake(withContext: Any?)](wkinterfacecontroller/awake(withcontext:).md)
  Initializes the interface controller with the specified context data.
- [func setTitle(String?)](wkinterfacecontroller/settitle(_:).md)
  Sets the title of the interface.
### Responding to activation and appearance events
- [func willActivate()](wkinterfacecontroller/willactivate.md)
  Tells the interface controller that the system is about to activate its view.
- [func didDeactivate()](wkinterfacecontroller/diddeactivate.md)
  Tells the interface controller that its view is no longer active.
- [func didAppear()](wkinterfacecontroller/didappear.md)
  Tells the interface controller that its view is now onscreen.
- [func willDisappear()](wkinterfacecontroller/willdisappear.md)
  Tells the interface controller that its view is now offscreen.
### Implementing a navigation interface
- [func pushController(withName: String, context: Any?)](wkinterfacecontroller/pushcontroller(withname:context:).md)
  Pushes a new interface controller onto the screen.
- [func pop()](wkinterfacecontroller/pop.md)
  Pops the current interface controller from the screen.
- [func popToRootController()](wkinterfacecontroller/poptorootcontroller.md)
  Pops all interface controllers except the app’s initial interface controller.
### Presenting interface controllers modally
- [func presentController(withName: String, context: Any?)](wkinterfacecontroller/presentcontroller(withname:context:).md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/presentcontroller(withnames:contexts:).md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(withnamesandcontexts:).md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:).md)
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.
- [func dismiss()](wkinterfacecontroller/dismiss.md)
  Dismisses the current interface controller from the screen.
### Navigating a page-based interface
- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [enum WKPageOrientation](wkpageorientation.md)
  Scrolling orientations for page-based interfaces.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](wkinterfacecontroller/becomecurrentpage.md)
  Displays the interface controller in the page-based interface.
### Managing segue-based transitions
- [func contextForSegue(withIdentifier: String) -> Any?](wkinterfacecontroller/contextforsegue(withidentifier:).md)
  Returns the context object to pass to the specified interface controller when a button is tapped.
- [func contextsForSegue(withIdentifier: String) -> [Any]?](wkinterfacecontroller/contextsforsegue(withidentifier:).md)
  Returns the context objects to pass to a page-based set of interface controllers when a button is tapped.
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:).md)
  Returns the context object to pass to the specified interface controller when a row in a table is tapped.
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:).md)
  Returns the context objects to pass to a page-based set of interface controllers when a row in a table is tapped.
### Managing Scrolling
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](wkinterfacecontroller/scroll(to:at:animated:).md)
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md)
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](wkinterfacecontroller/interfacedidscrolltotop.md)
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](wkinterfacecontroller/interfaceoffsetdidscrolltotop.md)
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](wkinterfacecontroller/interfaceoffsetdidscrolltobottom.md)
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](wkinterfacecontroller/istablescrollinghapticfeedbackenabled.md)
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.
### Respecting safe areas and layout margins
- [var contentSafeAreaInsets: UIEdgeInsets](wkinterfacecontroller/contentsafeareainsets.md)
  Insets that define the area where it’s safe to display content on the screen.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](wkinterfacecontroller/systemminimumlayoutmargins.md)
  Leading and trailing insets that represent the minimum layout margins for text elements.
- [var contentFrame: CGRect](wkinterfacecontroller/contentframe.md)
  The frame rectangle used to display your app’s content.
### Animating changes to the interface
- [func animate(withDuration: TimeInterval, animations: () -> Void)](wkinterfacecontroller/animate(withduration:animations:).md)
  Animates changes to one or more interface objects over the specified duration.
### Handling text input
- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md)
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md)
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](wkinterfacecontroller/dismisstextinputcontroller.md)
  Dismisses the text input controller without returning any text.
- [enum WKTextInputMode](wktextinputmode.md)
  The input modes supported by the text input controller.
### Presenting video and audio interfaces
- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:).md)
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md)
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](wkinterfacecontroller/dismissmediaplayercontroller.md)
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md)
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md)
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md)
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](wkinterfacecontroller/dismissaudiorecordercontroller.md)
  Dismisses the audio recording interface controller.
### Handling table-row selections
- [func table(WKInterfaceTable, didSelectRowAt: Int)](wkinterfacecontroller/table(_:didselectrowat:).md)
  Called to let you know that the user selected a row in the table.
### Managing pickers
- [func pickerDidFocus(WKInterfacePicker)](wkinterfacecontroller/pickerdidfocus(_:).md)
  Called to let you know that the specified picker is now receiving input from the Digital Crown.
- [func pickerDidResignFocus(WKInterfacePicker)](wkinterfacecontroller/pickerdidresignfocus(_:).md)
  Called to let you know that the specified picker is no longer receiving input from the Digital Crown.
- [func pickerDidSettle(WKInterfacePicker)](wkinterfacecontroller/pickerdidsettle(_:).md)
  Called to let you know when the user settles on a value in a picker.
### Getting the crown sequencer
- [var crownSequencer: WKCrownSequencer](wkinterfacecontroller/crownsequencer.md)
  The object to use when directly tracking crown events.
### Coordinating Handoff activity
- [func update(NSUserActivity)](wkinterfacecontroller/update(_:).md)
  Registers the current user activity with the system.
- [func invalidateUserActivity()](wkinterfacecontroller/invalidateuseractivity.md)
  Invalidates the most recent user activity.
### Adding PassKit passes
- [func presentAddPassesController(withPasses: [PKPass], completion: () -> Void)](wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:).md)
  Displays a modal interface for presenting passes to the user.
- [func dismissAddPassesController()](wkinterfacecontroller/dismissaddpassescontroller.md)
  Dismisses the pass interface controller
### Managing Notifications
- [let WKAccessibilityVoiceOverStatusChanged: String](wkaccessibilityvoiceoverstatuschanged.md)
  Tells the interface controller that the VoiceOver status has changed.
### Deprecated symbols
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
- [enum WKMenuItemIcon](wkmenuitemicon.md)
  Template images that you can use for menus.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [WKUserNotificationInterfaceController](wkusernotificationinterfacecontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md)
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md)
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKAlertAction](wkalertaction.md)
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md)
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)*