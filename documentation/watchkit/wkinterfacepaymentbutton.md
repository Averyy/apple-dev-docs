# WKInterfacePaymentButton

**Framework**: WatchKit  
**Kind**: class

A button that you can use to trigger payments through Apple Pay.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
class WKInterfacePaymentButton
```

#### Overview

Use a payment button to initiate an Apple Pay transaction on Apple Watch.

![A screenshot of the Apple Pay Button.](https://docs-assets.developer.apple.com/published/7edb9f4e5d0ba2fc72a5b546d35494a5/media-2930172%402x.png)

> **Note**:  The payment button (see [`Figure 1`](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton#2930172)) does not create or process payments. It simply provides a button with the Apple Pay mark. You must connect this button to an action method that creates an Apple Pay payment request. For more information on using the Apple Pay mark, see [`Apple Pay Identity Guidelines`](https://developer.apple.comhttps://developer.apple.com/apple-pay/Apple-Pay-Identity-Guidelines.pdf).

 The payment button (see [`Figure 1`](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton#2930172)) does not create or process payments. It simply provides a button with the Apple Pay mark. You must connect this button to an action method that creates an Apple Pay payment request. For more information on using the Apple Pay mark, see [`Apple Pay Identity Guidelines`](https://developer.apple.comhttps://developer.apple.com/apple-pay/Apple-Pay-Identity-Guidelines.pdf).

Do not subclass or create instances of this class yourself. Instead, drag a Payment Button object from your Object Library and add it to your storyboard. Then define an outlet in your interface controller class and connect it to the payment button object.

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the payment button. This class does not provide any new public methods or properties. However, it does inherit the methods and properties of its superclass, the [`WKInterfaceObject`](https://developer.apple.com/documentation/watchkit/wkinterfaceobject) class.

To respond to taps in the payment button, declare a method of this form in the interface controller class that manages the button:

You can change the name of your action method to anything you like. In your Xcode storyboard, connect the button’s selector to the custom action method defined in your class. In the action method, create the payment request and present the payment sheet by calling a [`PKPaymentAuthorizationController`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationController) object’s [`present(completion:)`](https://developer.apple.com/documentation/PassKit/PKPaymentAuthorizationController/present(completion:)) method.

Payment buttons can be used only to initiate Apple Pay transactions.

## Topics

### Initializing for SwiftUI
- [init(target: Any?, action: Selector)](init(target:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton/init(target:action:)))
  Creates a payment button for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton)*