# WKInterfaceAuthorizationAppleIDButton

**Framework**: Watchkit  
**Kind**: class

A button that you can use to trigger a Sign in with Apple request.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
class WKInterfaceAuthorizationAppleIDButton
```

#### Overview

Use the authorization button to initiate Sign in with Apple on Apple Watch. You can’t use this button to do anything other than initiating sign-in requests.

> **Note**:  The authorization button doesn’t perform the sign-in request; it provides a button with the correct branding. You must connect this button to an action method to perform the actual request. For more information, see [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).

 The authorization button doesn’t perform the sign-in request; it provides a button with the correct branding. You must connect this button to an action method to perform the actual request. For more information, see [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).

Don’t subclass or create instances of this class yourself. Instead, drag the button from the Object library and add it to your storyboard. Then define an outlet in your interface controller class and connect it to the button object.

While initializing the interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the button (for example, hiding or disabling the button). This class inherits the methods and properties from its superclass, the [`WKInterfaceObject`](wkinterfaceobject.md) class.

To respond to authorization button taps, connect the interface object in the storyboard to an action method in the interface controller:

In the action method, create a sign-in request using the authorization provider, and then use an instance of [`ASAuthorizationController`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationController) to execute the request.

## Topics

### Initializing for SwiftUI
- [init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)](wkinterfaceauthorizationappleidbutton/init(style:target:action:).md)
  Creates an authorization button for use in SwiftUI.
- [WKInterfaceAuthorizationAppleIDButton.Style](wkinterfaceauthorizationappleidbutton/style.md)
  Values that define an authorization button’s style.
- [init(target: Any?, action: Selector)](wkinterfaceauthorizationappleidbutton/init(target:action:).md)
  Creates an authorization button for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md)
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md)
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md)
  A button in the user interface of your watchOS app.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md)
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md)
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md)
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md)
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](wkinterfacemap.md)
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton)*