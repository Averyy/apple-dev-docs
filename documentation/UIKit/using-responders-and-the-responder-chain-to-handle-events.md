# Using responders and the responder chain to handle events

**Framework**: UIKit

Learn how to handle events that propagate through your app.

#### Overview

Apps receive and handle events using . A responder object is any instance of the [`UIResponder`](uiresponder.md) class, and common subclasses include [`UIView`](uiview.md), [`UIViewController`](uiviewcontroller.md), and [`UIApplication`](uiapplication.md). Responders receive the raw event data and must either handle the event or forward it to another responder object. When your app receives an event, UIKit automatically directs that event to the most appropriate responder object, known as the .

Unhandled events are passed from responder to responder in the active , which is the dynamic configuration of your app’s responder objects. The following image shows the responders in an app whose interface contains a label, a text field, a button, and two background views. The diagram also shows how events move from one responder to the next, following the responder chain.

![A flow diagram: On the left, a sample app contains a label (UILabel), a text field for the user to input text (UITextField), and a button (UIButton) to  press after entering text in the field. On the right, the flow diagram shows how, after the user pressed the button, the event moves through the responder chain — from UIView, to UIViewController, to UIWindow, UIApplication, and finally to UIApplicationDelegate.](https://docs-assets.developer.apple.com/published/5c87414d0f580b2563835705a3198449/media-3004381%402x.png)

If the text field doesn’t handle an event, UIKit sends the event to the text field’s parent [`UIView`](uiview.md) object, followed by the root view of the window. From the root view, the responder chain diverts to the owning view controller before directing the event to the window. If the window can’t handle the event, UIKit delivers the event to the [`UIApplication`](uiapplication.md) object, and possibly to the app delegate if that object is an instance of [`UIResponder`](uiresponder.md) and not already part of the responder chain.

##### Determine an Events First Responder

UIKit designates an object as the first responder to an event based on the type of that event. Event types include:

| Event type | First responder |
| --- | --- |
| Touch events | The view in which the touch occurred. |
| Press events | The object that has focus. |
| Shake-motion events | The object that you (or UIKit) designate. |
| Remote-control events | The object that you (or UIKit) designate. |
| Editing menu messages | The object that you (or UIKit) designate. |

> **Note**:  Motion events related to the accelerometers, gyroscopes, and magnetometer don’t follow the responder chain. Instead, Core Motion delivers those events directly to the designated object. For more information, see [`Core Motion Framework`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iPhoneOSTechOverview/CoreServicesLayer/CoreServicesLayer.html#//apple_ref/doc/uid/TP40007898-CH10-SW27)

Controls communicate directly with their associated target object using action messages. When the user interacts with a control, the control sends an action message to its target object. Action messages aren’t events, but they may still take advantage of the responder chain. When the target object of a control is `nil`, UIKit starts from the target object and traverses the responder chain until it finds an object that implements the appropriate action method. For example, the UIKit editing menu uses this behavior to search for responder objects that implement methods with names like [`cut(_:)`](uiresponderstandardeditactions/cut(_:).md), [`copy(_:)`](uiresponderstandardeditactions/copy(_:).md), or [`paste(_:)`](uiresponderstandardeditactions/paste(_:).md).

Gesture recognizers receive touch and press events before their view does. If a view’s gesture recognizers fail to recognize a sequence of touches, UIKit sends the touches to the view. If the view doesn’t handle the touches, UIKit passes them up the responder chain. For more information about using gesture recognizer’s to handle events, see [`Handling UIKit gestures`](handling-uikit-gestures.md).

##### Determine Which Responder Contained a Touch Event

UIKit uses view-based hit-testing to determine where touch events occur. Specifically, UIKit compares the touch location to the bounds of view objects in the view hierarchy. The [`hitTest(_:with:)`](uiview/hittest(_:with:).md) method of [`UIView`](uiview.md) traverses the view hierarchy, looking for the deepest subview that contains the specified touch, which becomes the first responder for the touch event.

> **Note**:  If a touch location is outside of a view’s bounds, the [`hitTest(_:with:)`](uiview/hittest(_:with:).md) method ignores that view and all of its subviews. As a result, when a view’s [`clipsToBounds`](uiview/clipstobounds.md) property is [`true`](https://developer.apple.com/documentation/swift/true), subviews outside of that view’s bounds aren’t returned even if they happen to contain the touch. For more information about the hit-testing behavior, see the discussion of the [`hitTest(_:with:)`](uiview/hittest(_:with:).md) method in [`UIView`](uiview.md).

When a touch occurs, UIKit creates a [`UITouch`](uitouch.md) object and associates it with a view. As the touch location or other parameters change, UIKit updates the same [`UITouch`](uitouch.md) object with the new information. The only property that doesn’t change is the view. (Even when the touch location moves outside the original view, the value in the touch’s [`view`](uitouch/view.md) property doesn’t change). When the touch ends, UIKit releases the [`UITouch`](uitouch.md) object.

##### Alter the Responder Chain

You can alter the responder chain by overriding the [`next`](uiresponder/next.md) property of your responder objects. When you do this, the next responder is the object that you return.

Many UIKit classes already override this property and return specific objects, including:

- [`UIView`](uiview.md) objects. If the view is the root view of a view controller, the next responder is the view controller; otherwise, the next responder is the view’s superview.
- [`UIViewController`](uiviewcontroller.md) objects.
- If the view controller’s view is the root view of a window, the next responder is the window object.
- If the view controller was presented by another view controller, the next responder is the presenting view controller.
- [`UIWindow`](uiwindow.md) objects. The window’s next responder is the [`UIApplication`](uiapplication.md) object.
- [`UIApplication`](uiapplication.md) object. The next responder is the app delegate, but only if the app delegate is an instance of [`UIResponder`](uiresponder.md) and isn’t a view, view controller, or the app object itself.

## See Also

- [class UIResponder](uiresponder.md)
  An abstract interface for responding to and handling events.
- [class UIEvent](uievent.md)
  An object that describes a single user interaction with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/using-responders-and-the-responder-chain-to-handle-events)*