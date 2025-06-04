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

## Overview

Use the authorization button to initiate Sign in with Apple on Apple Watch. You can’t use this button to do anything other than initiating sign-in requests.

> **Note**:  The authorization button doesn’t perform the sign-in request; it provides a button with the correct branding. You must connect this button to an action method to perform the actual request. For more information, see [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).

 The authorization button doesn’t perform the sign-in request; it provides a button with the correct branding. You must connect this button to an action method to perform the actual request. For more information, see [`Authentication Services`](https://developer.apple.com/documentation/AuthenticationServices).

Don’t subclass or create instances of this class yourself. Instead, drag the button from the Object library and add it to your storyboard. Then define an outlet in your interface controller class and connect it to the button object.

While initializing the interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the button (for example, hiding or disabling the button). This class inherits the methods and properties from its superclass, the [`WKInterfaceObject`](https://developer.apple.com/documentation/watchkit/wkinterfaceobject) class.

To respond to authorization button taps, connect the interface object in the storyboard to an action method in the interface controller:

In the action method, create a sign-in request using the authorization provider, and then use an instance of [`ASAuthorizationController`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationController) to execute the request.

## Topics

### Initializing for SwiftUI
- [init(style: WKInterfaceAuthorizationAppleIDButton.Style, target: Any?, action: Selector)](init(style:target:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(style:target:action:)))
  Creates an authorization button for use in SwiftUI.
- [WKInterfaceAuthorizationAppleIDButton.Style](style.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/style))
  Values that define an authorization button’s style.
- [init(target: Any?, action: Selector)](init(target:action:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton/init(target:action:)))
  Creates an authorization button for use in SwiftUI.

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
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton)*