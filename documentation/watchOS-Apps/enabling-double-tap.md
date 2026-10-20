# Enabling the double-tap gesture on Apple Watch

**Framework**: watchOS apps  
**Role**: Article

Customize your app’s response to the double-tap gesture on Apple Watch.

#### Overview

On Apple Watch Series 9 and Apple Watch Ultra 2, people can trigger a scene’s primary action by tapping their index finger and thumb together twice. In watchOS 11 and later, you can assign a buttonlike control, such as a [`Button`](../SwiftUI/button.md) or [`Toggle`](../SwiftUI/toggle.md) as the scene’s primary action, customizing how your app responds to double tap.

##### Take advantage of system behaviors

Your app receives the default double-tap behaviors automatically. With double tap, people can scroll through lists and scroll views. They can also page through a vertical tab bar. In general, if your scene contains lists, vertical tab views, or scroll views, the system can handle the gesture for your app.

##### Declare a primary action

If your scene has an obvious main action, you can designate it as the primary action using the [`handGestureShortcut(_:isEnabled:)`](../SwiftUI/view/handgestureshortcut%28_,isenabled%29.md) modifier and passing the [`primaryAction`](../SwiftUI/handgestureshortcut/primaryaction.md) as the parameter.

```swift
Button ("Start Activity") {
    startActivity = true
}
// Set this button as the primary action for double tap.
.handGestureShortcut(.primaryAction)
```

When double tap triggers your primary action, the system automatically highlights the affected control. It calculates the shape of the highlighted area based on the control’s content. If you need to customize the highlight, use a [`clipShape(_:style:)`](../SwiftUI/view/clipshape%28_,style%29.md) to modify the control’s shape.

You can add the primary action modifier to any buttonlike control, such as buttons, toggles, navigation links, or text fields. You can even add it to widgets and live activities that appear in the Smart Stack, including remote live activities from iOS. However, you can only assign one primary action per scene. If the scene has multiple items that can interact with double tap, such as a primary action inside a scroll view, the system determines the effect based on the following priorities:

1. Primary action
2. Scroll view
3. Vertical tab pagination

> ❗ **Important**: Double tap only triggers your primary action if the control is on screen. Otherwise, the system scrolls towards the control one page at a time.

The [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/gestures#watchOS) has additional design guidance.

## See Also

### Related Documentation
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)
  A gesture is a physical motion that a person uses to directly affect an object in an app or game on their device.
- [func handGestureShortcut(HandGestureShortcut, isEnabled: Bool) -> some View
](../SwiftUI/view/handgestureshortcut%28_,isenabled%29.md)
  Assigns a hand gesture shortcut to the modified control.
- [static let primaryAction: HandGestureShortcut](../SwiftUI/handgestureshortcut/primaryaction.md)
  The hand gesture shortcut for the primary action.
- [func clipShape<S>(S, style: FillStyle) -> some View
](../SwiftUI/view/clipshape%28_,style%29.md)
  Sets a clipping shape for this view.
- [static var verticalPage: VerticalPageTabViewStyle](../SwiftUI/tabviewstyle/verticalpage.md)
  A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
### App experience
- [Setting up a watchOS project](./setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [Creating independent watchOS apps](./creating-independent-watchos-apps.md)
  Set up a watchOS app that installs and runs without a companion iOS app.
- [Keeping your watchOS content up to date](./keeping-your-watchos-app-s-content-up-to-date.md)
  Ensure that your app’s content is relevant and up to date.
- [Updating watchOS apps with timelines](./updating-watchos-apps-with-timelines.md)
  Seamlessly schedule updates to your user interface, even while it’s inactive.
- [Authenticating users on Apple Watch](./authenticating-users-on-apple-watch.md)
  Create an account sign-up and sign-in strategy for your app.
- [Responding to the Action button on Apple Watch Ultra](../AppIntents/actionbuttonarticle.md)
  Use App Intents to register actions for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/enabling-double-tap)*