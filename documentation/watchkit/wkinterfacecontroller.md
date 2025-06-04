# WKInterfaceController

**Framework**: Watchkit  
**Kind**: class

A class that provides the infrastructure for managing the interface in a watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor class WKInterfaceController
```

## Overview

An interface controller serves the same purpose as a [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) object in a UIKit app, except that it doesn’t manage any actual views. It runs in your WatchKit extension and remotely manages the behavior associated with an interface controller in your Watch app’s storyboard file. You subclass [`WKInterfaceController`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller) and use its methods to configure the elements of your storyboard scene and to respond to interactions with those elements.

Your interface controller code runs locally on the user’s Apple Watch but is separate from the interface that it manages. When you change the value of an interface object in your code, the system forwards the needed information to your Watch app, which makes the corresponding changes onscreen.

When the user interacts with your app content, the system launches your extension and creates the appropriate interface controller objects automatically. Apps use different interface controllers to manage their notification and app interfaces; WatchKit uses the information in your app’s main storyboard file to determine which interface controller to load. Notification scenes are configured specially so that the system can identify them. For your app, WatchKit loads your app’s main interface controller initially, but you may change the initial interface controller at launch time.

When creating an interface controller, WatchKit instantiates the class and calls its [`init()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init()) method. You can use this method to initialize variables and load data; however, don’t use it to configure your user interface. The controller’s user interface elements may not be properly initialized when this method runs.

Next, the system calls the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method. If WatchKit passes a valid object to the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method, use the information in that object to customize the initialization process. Also, the controller’s user interface elements are guaranteed to be available at this point. This means that you can safely use this method to configure your user interface.

The [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method lets you know when your interface is about to become active. Use the [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method to perform any last minute tasks, such as checking for updates to your content; however, don’t use it for your primary initialization.

The [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method may be called at times when your interface isn’t yet onscreen. For example, WatchKit may call the method in advance so that you have time to update your content. WatchKit calls the [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()) method to let you know when your interface becomes visible. Similarly, WatchKit calls the [`willDisappear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear()) and [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) methods when your interface moves offscreen again.

> ❗ **Important**:  An interface controller can make changes to its interface only in the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method, in the [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method, and while the interface is active. Once the system calls the [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method, it ignores any attempts to change the value of the controller’s interface objects until the system calls the interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method again.

 An interface controller can make changes to its interface only in the [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method, in the [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method, and while the interface is active. Once the system calls the [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method, it ignores any attempts to change the value of the controller’s interface objects until the system calls the interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method again.

In iOS Simulator, WatchKit calls the [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method for the current interface controller when you lock the simulator by selecting Hardware > Lock. When you subsequently unlock the simulator, WatchKit calls that interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method again. You can use this capability to debug your activation and deactivation code.

Xcode lets you configure information about your interface controller in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Description'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Identifier'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The name of the interface controller. Use this name to specify which interface controller to push or present.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Title', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The title string assigned to the interface controller. You can set this value programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceController/setTitle(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Is Initial Controller'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A Boolean indicating whether the object is the app’s root interface controller. Only one interface controller at a time may have this option enabled. This option doesn’t apply to glance or notification interface controllers.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Activity Indicator On Load', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A Boolean value that indicates whether the interface controller’s contents are hidden until the '}, {'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceController/willActivate()', 'isActive': True}, {'type': 'text', 'text': ' method returns. When you enable this option, the system displays a progress indicator until the '}, {'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceController/willActivate()', 'isActive': True}, {'type': 'text', 'text': ' method returns. You might disable this option if your interface contains mostly static information that can be displayed right away.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Always Bounce'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A Boolean value that turns off scrolling and allows built-in controls and containers to fill content to the screen edges, regardless of the content-safe area.'}]}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Full Screen'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'A Boolean value that determines whether SpriteKit or SceneKit content can use the full screen. The system hides the status bar but displays the time in the upper-right corner with a gradient behind it, making the time clearly visible against the scene.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Fixed to screen edges'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'A Boolean value that indicates whether the contents ignore the safe area and minimum layout margins. When you enable this option, the system turns off scrolling, and allows built-in controls and containers to fill content to the screen edges.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Background', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The background image displayed behind the scene’s content. The image specified in your storyboard scrolls with your interface controller’s content.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Mode'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The content mode for the background image. This mode defines how the background image scales or fills the screen and behaves in the same way as the constants for the '}, {'type': 'reference', 'identifier': 'doc://com.apple.documentation/documentation/UIKit/UIView/ContentMode-swift.enum', 'isActive': True}, {'text': ' type.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Animate'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'A Boolean value indicating whether an animated background image starts running its animation automatically after being loaded. Set this option to ', 'type': 'text'}, {'code': 'Yes', 'type': 'codeVoice'}, {'text': ' if you want the animation to start automatically; set it to ', 'type': 'text'}, {'code': 'No', 'type': 'codeVoice'}, {'text': ' if you prefer to start the animation programmatically.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Color'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The background color to be displayed behind the scene’s content.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Insets', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The amount of space (in points) to insert between the edges of the interface controller and its content. Select Custom to specify different values for the top, bottom, left, and right edges.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Spacing', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Additional spacing (in points) to include between items in the interface controller.', 'type': 'text'}], 'type': 'paragraph'}] |

Subclass `WKInterfaceController` when you have a storyboard scene that requires configuration at runtime or that handles user interactions. Typically, you define a custom subclass for each unique storyboard scene that your app manages. In your subclass, define outlets for any interface objects you need to configure and define action methods for responding to interactions with the elements of your storyboard scene.

Most custom interface controllers you use in your app require a custom interface controller subclass. Even glances need an interface controller to update the glance contents. The only storyboard scene that can’t use a custom interface controller is the scene associated with a static notification interface. When implementing an interface controller for your dynamic notification interface, subclass [`WKUserNotificationInterfaceController`](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller) instead.

Override any methods of the class needed to configure your interface and get it ready to display. Most interface controllers override the [`init()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init()) and [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) methods. Override any other methods that make sense based on your needs.

## Topics

### Creating the interface controller
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/init()))
  Returns an initialized interface controller object.
- [func awake(withContext: Any?)](awake(withcontext:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)))
  Initializes the interface controller with the specified context data.
- [func setTitle(String?)](settitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:)))
  Sets the title of the interface.
### Responding to activation and appearance events
- [func willActivate()](willactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()))
  Tells the interface controller that the system is about to activate its view.
- [func didDeactivate()](diddeactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()))
  Tells the interface controller that its view is no longer active.
- [func didAppear()](didappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()))
  Tells the interface controller that its view is now onscreen.
- [func willDisappear()](willdisappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear()))
  Tells the interface controller that its view is now offscreen.
### Implementing a navigation interface
- [func pushController(withName: String, context: Any?)](pushcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pushcontroller(withname:context:)))
  Pushes a new interface controller onto the screen.
- [func pop()](pop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pop()))
  Pops the current interface controller from the screen.
- [func popToRootController()](poptorootcontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/poptorootcontroller()))
  Pops all interface controllers except the app’s initial interface controller.
### Presenting interface controllers modally
- [func presentController(withName: String, context: Any?)](presentcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:)))
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](presentcontroller(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:)))
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](presentcontroller(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnamesandcontexts:)))
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](presentalert(withtitle:message:preferredstyle:actions:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)))
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle))
  Constants indicating the styles for standard system alerts.
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()))
  Dismisses the current interface controller from the screen.
### Navigating a page-based interface
- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [enum WKPageOrientation](wkpageorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation))
  Scrolling orientations for page-based interfaces.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](reloadrootcontrollers(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](becomecurrentpage().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/becomecurrentpage()))
  Displays the interface controller in the page-based interface.
### Managing segue-based transitions
- [func contextForSegue(withIdentifier: String) -> Any?](contextforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:)))
  Returns the context object to pass to the specified interface controller when a button is tapped.
- [func contextsForSegue(withIdentifier: String) -> [Any]?](contextsforsegue(withidentifier:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:)))
  Returns the context objects to pass to a page-based set of interface controllers when a button is tapped.
- [func contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](contextforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextforsegue(withidentifier:in:rowindex:)))
  Returns the context object to pass to the specified interface controller when a row in a table is tapped.
- [func contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](contextsforsegue(withidentifier:in:rowindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contextsforsegue(withidentifier:in:rowindex:)))
  Returns the context objects to pass to a page-based set of interface controllers when a row in a table is tapped.
### Managing Scrolling
- [func scroll(to: WKInterfaceObject, at: WKInterfaceScrollPosition, animated: Bool)](scroll(to:at:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/scroll(to:at:animated:)))
  Scrolls the specified object to the given position onscreen.
- [enum WKInterfaceScrollPosition](wkinterfacescrollposition.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescrollposition))
  Onscreen scroll positions.
- [func interfaceDidScrollToTop()](interfacedidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfacedidscrolltotop()))
  Tells the interface controller that the user has performed a scroll-to-top gesture (for example, tapping the status bar) and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToTop()](interfaceoffsetdidscrolltotop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltotop()))
  Tells the interface controller that the user has scrolled to the top of the interface and that the scrolling animation has finished.
- [func interfaceOffsetDidScrollToBottom()](interfaceoffsetdidscrolltobottom().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/interfaceoffsetdidscrolltobottom()))
  Tells the interface controller that the user has scrolled to the bottom of the interface and that the scrolling animation has finished.
- [var isTableScrollingHapticFeedbackEnabled: Bool](istablescrollinghapticfeedbackenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/istablescrollinghapticfeedbackenabled))
  A Boolean value that determines whether haptic feedback coordinates with the appearance of new rows as the user scrolls through a table.
### Respecting safe areas and layout margins
- [var contentSafeAreaInsets: UIEdgeInsets](contentsafeareainsets.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentsafeareainsets))
  Insets that define the area where it’s safe to display content on the screen.
- [var systemMinimumLayoutMargins: NSDirectionalEdgeInsets](systemminimumlayoutmargins.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/systemminimumlayoutmargins))
  Leading and trailing insets that represent the minimum layout margins for text elements.
- [var contentFrame: CGRect](contentframe.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/contentframe))
  The frame rectangle used to display your app’s content.
### Animating changes to the interface
- [func animate(withDuration: TimeInterval, animations: () -> Void)](animate(withduration:animations:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/animate(withduration:animations:)))
  Animates changes to one or more interface objects over the specified duration.
### Handling text input
- [func presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontroller(withsuggestions:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontroller(withsuggestions:allowedinputmode:completion:)))
  Displays a modal interface for gathering text input from the user.
- [func presentTextInputControllerWithSuggestions(forLanguage: ((String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Void)](presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presenttextinputcontrollerwithsuggestions(forlanguage:allowedinputmode:completion:)))
  Displays a modal interface for gathering language-specific text input from the user.
- [func dismissTextInputController()](dismisstextinputcontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismisstextinputcontroller()))
  Dismisses the text input controller without returning any text.
- [enum WKTextInputMode](wktextinputmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextinputmode))
  The input modes supported by the text input controller.
### Presenting video and audio interfaces
- [func presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, (any Error)?) -> Void)](presentmediaplayercontroller(with:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentmediaplayercontroller(with:options:completion:)))
  Displays a modal interface for playing the specified media file.
- [Media Player Options](media-player-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/media-player-options))
  Keys indicating media playback options.
- [func dismissMediaPlayerController()](dismissmediaplayercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissmediaplayercontroller()))
  Dismisses the media interface controller.
- [func presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, (any Error)?) -> Void)](presentaudiorecordercontroller(withoutputurl:preset:options:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaudiorecordercontroller(withoutputurl:preset:options:completion:)))
  Display a standard interface for recording audio from the user’s Apple Watch.
- [enum WKAudioRecorderPreset](wkaudiorecorderpreset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset))
  Constants indicating the quality of audio recordings.
- [Audio Recording Options](audio-recording-options.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/audio-recording-options))
  Options to specify when recording audio.
- [func dismissAudioRecorderController()](dismissaudiorecordercontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaudiorecordercontroller()))
  Dismisses the audio recording interface controller.
### Handling table-row selections
- [func table(WKInterfaceTable, didSelectRowAt: Int)](table(_:didselectrowat:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/table(_:didselectrowat:)))
  Called to let you know that the user selected a row in the table.
### Managing pickers
- [func pickerDidFocus(WKInterfacePicker)](pickerdidfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidfocus(_:)))
  Called to let you know that the specified picker is now receiving input from the Digital Crown.
- [func pickerDidResignFocus(WKInterfacePicker)](pickerdidresignfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidresignfocus(_:)))
  Called to let you know that the specified picker is no longer receiving input from the Digital Crown.
- [func pickerDidSettle(WKInterfacePicker)](pickerdidsettle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidsettle(_:)))
  Called to let you know when the user settles on a value in a picker.
### Getting the crown sequencer
- [var crownSequencer: WKCrownSequencer](crownsequencer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/crownsequencer))
  The object to use when directly tracking crown events.
### Coordinating Handoff activity
- [func update(NSUserActivity)](update(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/update(_:)))
  Registers the current user activity with the system.
- [func invalidateUserActivity()](invalidateuseractivity().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/invalidateuseractivity()))
  Invalidates the most recent user activity.
### Adding PassKit passes
- [func presentAddPassesController(withPasses: [PKPass], completion: () -> Void)](presentaddpassescontroller(withpasses:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:)))
  Displays a modal interface for presenting passes to the user.
- [func dismissAddPassesController()](dismissaddpassescontroller().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaddpassescontroller()))
  Dismisses the pass interface controller
### Managing Notifications
- [let WKAccessibilityVoiceOverStatusChanged: String](wkaccessibilityvoiceoverstatuschanged.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityvoiceoverstatuschanged))
  Tells the interface controller that the VoiceOver status has changed.
### Deprecated symbols
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
- [enum WKMenuItemIcon](wkmenuitemicon.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkmenuitemicon))
  Template images that you can use for menus.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Inherited By
- [WKUserNotificationInterfaceController](wkusernotificationinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)*