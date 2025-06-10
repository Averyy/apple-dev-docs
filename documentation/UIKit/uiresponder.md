# UIResponder

**Framework**: UIKit  
**Kind**: class

An abstract interface for responding to and handling events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIResponder
```

## Mentions

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md)

#### Overview

Responder objects — instances of [`UIResponder`](uiresponder.md) — constitute the event-handling backbone of a UIKit app. Many key objects are also responders, including the [`UIApplication`](uiapplication.md) object, [`UIViewController`](uiviewcontroller.md) objects, and all [`UIView`](uiview.md) objects (which includes [`UIWindow`](uiwindow.md)). As events occur, UIKit dispatches them to your app’s responder objects for handling.

There are several kinds of events, including touch events, motion events, remote-control events, and press events. To handle a specific type of event, a responder must override the corresponding methods. For example, to handle touch events, a responder implements the [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md), [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md), [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md), and [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) methods. In the case of touches, the responder uses the event information provided by UIKit to track changes to those touches and to update the app’s interface appropriately.

In addition to handling events, UIKit responders also manage the forwarding of unhandled events to other parts of your app. If a given responder doesn’t handle an event, it forwards that event to the next event in the responder chain. UIKit manages the responder chain dynamically, using predefined rules to determine which object should be next to receive an event. For example, a view forwards events to its superview, and the root view of a hierarchy forwards events to its view controller.

Responders process [`UIEvent`](uievent.md) objects but can also accept custom input through an input view. The system’s keyboard is the most obvious example of an input view. When the user taps a [`UITextField`](uitextfield.md) and [`UITextView`](uitextview.md) object onscreen, the view becomes the first responder and displays its input view, which is the system keyboard. Similarly, you can create custom input views and display them when other responders become active. To associate a custom input view with a responder, assign that view to the [`inputView`](uiresponder/inputview.md) property of the responder.

For information about responders and the responder chain, see [`Using responders and the responder chain to handle events`](using-responders-and-the-responder-chain-to-handle-events.md).

## Topics

### Managing the responder chain
- [var next: UIResponder?](uiresponder/next.md)
  Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [var isFirstResponder: Bool](uiresponder/isfirstresponder.md)
  Returns a Boolean value indicating whether this object is the first responder.
- [var canBecomeFirstResponder: Bool](uiresponder/canbecomefirstresponder.md)
  Returns a Boolean value indicating whether this object can become the first responder.
- [func becomeFirstResponder() -> Bool](uiresponder/becomefirstresponder.md)
  Asks UIKit to make this object the first responder in its window.
- [var canResignFirstResponder: Bool](uiresponder/canresignfirstresponder.md)
  Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [func resignFirstResponder() -> Bool](uiresponder/resignfirstresponder.md)
  Notifies this object that it has been asked to relinquish its status as first responder in its window.
### Responding to touch events
- [func touchesBegan(Set<UITouch>, with: UIEvent?)](uiresponder/touchesbegan(_:with:).md)
  Tells this object that one or more new touches occurred in a view or window.
- [func touchesMoved(Set<UITouch>, with: UIEvent?)](uiresponder/touchesmoved(_:with:).md)
  Tells the responder when one or more touches associated with an event changed.
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](uiresponder/touchesended(_:with:).md)
  Tells the responder when one or more fingers are raised from a view or window.
- [func touchesCancelled(Set<UITouch>, with: UIEvent?)](uiresponder/touchescancelled(_:with:).md)
  Tells the responder when a system event (such as a system alert) cancels a touch sequence.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](uiresponder/touchesestimatedpropertiesupdated(_:).md)
  Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.
### Responding to motion events
- [func motionBegan(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motionbegan(_:with:).md)
  Tells the responder that a motion event has begun.
- [func motionEnded(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motionended(_:with:).md)
  Tells the responder that a motion event has ended.
- [func motionCancelled(UIEvent.EventSubtype, with: UIEvent?)](uiresponder/motioncancelled(_:with:).md)
  Tells the responder that a motion event has been canceled.
### Responding to press events
- [func pressesBegan(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressesbegan(_:with:).md)
  Tells this object when a physical button is first pressed.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent?)](uiresponder/presseschanged(_:with:).md)
  Tells this object when a value associated with a press has changed.
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressesended(_:with:).md)
  Tells the object when a button is released.
- [func pressesCancelled(Set<UIPress>, with: UIPressesEvent?)](uiresponder/pressescancelled(_:with:).md)
  Tells this object when a system event (such as a low-memory warning) cancels a press event.
### Responding to remote-control events
- [func remoteControlReceived(with: UIEvent?)](uiresponder/remotecontrolreceived(with:).md)
  Tells the object when a remote-control event is received.
### Managing input views
- [var inputView: UIView?](uiresponder/inputview.md)
  The custom input view to display when the responder becomes the first responder.
- [var inputViewController: UIInputViewController?](uiresponder/inputviewcontroller.md)
  The custom input view controller to use when the responder becomes the first responder.
- [var inputAccessoryView: UIView?](uiresponder/inputaccessoryview.md)
  The custom input accessory view to display when the responder becomes the first responder.
- [var inputAccessoryViewController: UIInputViewController?](uiresponder/inputaccessoryviewcontroller.md)
  The custom input accessory view controller to display when the responder becomes the first responder.
- [func reloadInputViews()](uiresponder/reloadinputviews.md)
  Updates the custom input and accessory views when the object is the first responder.
### Getting the undo manager
- [var undoManager: UndoManager?](uiresponder/undomanager.md)
  Returns the nearest shared undo manager in the responder chain.
### Building and validating commands
- [func buildMenu(with: any UIMenuBuilder)](uiresponder/buildmenu(with:).md)
  Asks the receiving responder to add and remove items from a menu system.
- [func validate(UICommand)](uiresponder/validate(_:).md)
  Asks the receiving responder to validate the command.
- [func canPerformAction(Selector, withSender: Any?) -> Bool](uiresponder/canperformaction(_:withsender:).md)
  Requests the receiving responder to enable or disable the specified command in the user interface.
- [func target(forAction: Selector, withSender: Any?) -> Any?](uiresponder/target(foraction:withsender:).md)
  Returns the target object that responds to an action.
### Accessing the available key commands
- [var keyCommands: [UIKeyCommand]?](uiresponder/keycommands.md)
  The key commands that trigger actions on this responder.
### Managing the text input mode
- [var textInputMode: UITextInputMode?](uiresponder/textinputmode.md)
  The text input mode for this responder object.
- [var textInputContextIdentifier: String?](uiresponder/textinputcontextidentifier.md)
  An identifier signifying that the responder should preserve its text input mode information.
- [class func clearTextInputContextIdentifier(String)](uiresponder/cleartextinputcontextidentifier(_:).md)
  Clears text input mode information from the app’s user defaults.
- [var inputAssistantItem: UITextInputAssistantItem](uiresponder/inputassistantitem.md)
  The input assistant to use when configuring the keyboard’s shortcuts bar.
### Supporting user activities
- [var userActivity: NSUserActivity?](uiresponder/useractivity.md)
  An object encapsulating a user activity supported by this responder.
- [func restoreUserActivityState(NSUserActivity)](uiresponder/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](uiresponder/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.
### Managing activity items
- [var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)?](uiresponder/activityitemsconfiguration.md)
### Accessing the editing interaction
- [var editingInteractionConfiguration: UIEditingInteractionConfiguration](uiresponder/editinginteractionconfiguration.md)
- [enum UIEditingInteractionConfiguration](uieditinginteractionconfiguration.md)
### Capturing text from the camera
- [func captureTextFromCamera(Any?)](uiresponder/capturetextfromcamera(_:).md)
  Starts scanning text using the device’s camera.
### Managing the Touch Bar
- [func makeTouchBar() -> NSTouchBar?](uiresponder/maketouchbar.md)
  Asks the receiving responder to create and configure a Touch Bar object.
- [var touchBar: NSTouchBar?](uiresponder/touchbar.md)
  The Touch Bar object for the responder.
### Constants
- [class let keyboardAnimationCurveUserInfoKey: String](uiresponder/keyboardanimationcurveuserinfokey.md)
  A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [class let keyboardAnimationDurationUserInfoKey: String](uiresponder/keyboardanimationdurationuserinfokey.md)
  A user info key to retrieve the duration of the keyboard animation in seconds.
- [class let keyboardDidChangeFrameNotification: NSNotification.Name](uiresponder/keyboarddidchangeframenotification.md)
  A notification that posts immediately after a change in the keyboard’s frame.
- [class let keyboardDidHideNotification: NSNotification.Name](uiresponder/keyboarddidhidenotification.md)
  A notification that posts immediately after dismissing the keyboard.
- [class let keyboardDidShowNotification: NSNotification.Name](uiresponder/keyboarddidshownotification.md)
  A notification that posts immediately after displaying the keyboard.
- [class let keyboardFrameBeginUserInfoKey: String](uiresponder/keyboardframebeginuserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [class let keyboardFrameEndUserInfoKey: String](uiresponder/keyboardframeenduserinfokey.md)
  A user info key to retrieve the keyboard’s frame at the end of its animation.
- [class let keyboardIsLocalUserInfoKey: String](uiresponder/keyboardislocaluserinfokey.md)
  A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [class let keyboardWillChangeFrameNotification: NSNotification.Name](uiresponder/keyboardwillchangeframenotification.md)
  A notification that posts immediately prior to a change in the keyboard’s frame.
- [class let keyboardWillHideNotification: NSNotification.Name](uiresponder/keyboardwillhidenotification.md)
  A notification that posts immediately prior to dismissing the keyboard.
- [class let keyboardWillShowNotification: NSNotification.Name](uiresponder/keyboardwillshownotification.md)
  A notification that posts immediately prior to displaying the keyboard.
### Structures
- [UIResponder.KeyboardDidChangeFrameMessage](uiresponder/keyboarddidchangeframemessage.md)
- [UIResponder.KeyboardDidHideMessage](uiresponder/keyboarddidhidemessage.md)
- [UIResponder.KeyboardDidShowMessage](uiresponder/keyboarddidshowmessage.md)
- [UIResponder.KeyboardWillChangeFrameMessage](uiresponder/keyboardwillchangeframemessage.md)
- [UIResponder.KeyboardWillHideMessage](uiresponder/keyboardwillhidemessage.md)
- [UIResponder.KeyboardWillShowMessage](uiresponder/keyboardwillshowmessage.md)
### Instance Properties
- [var pencilKitResponderState: PKResponderState](uiresponder/pencilkitresponderstate.md)
  The PencilKit state associated with the responder object.
### Instance Methods
- [func provider(for: UIDeferredMenuElement) -> UIDeferredMenuElement.Provider?](uiresponder/provider(for:).md)
  Asks the responder for an element provider to fulfill the given focus-based deferred element. Check the `identifier` of the deferred element to identify which deferred element this is. By default, this returns nil. Return a non-nil `provider` to make this responder responsible for providing elements for this fulfillment of the deferred element.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIAccessibilityElement](uiaccessibilityelement.md)
- [UIApplication](uiapplication.md)
- [UIScene](uiscene.md)
- [UIView](uiview.md)
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
  Learn how to handle events that propagate through your app.
- [class UIEvent](uievent.md)
  An object that describes a single user interaction with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder)*