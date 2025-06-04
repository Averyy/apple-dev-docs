# WKInterfaceButton

**Framework**: WatchKit  
**Kind**: class

A button in the user interface of your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceButton
```

#### Overview

The content of a button’s tappable area is filled with text and an optional background color or image. When tapped by the user, the button calls its associated action method, which you define on the owning interface controller. Use that action method to initiate tasks and update your app’s interface.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a button object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen button.

To respond to taps in the button, declare a method of this form in the interface controller class that manages the button:

You can change the name of your action method to anything you like. In your Xcode storyboard, connect the button’s selector to the custom action method defined in your class.

##### Interface Builder Configuration Options

Xcode lets you configure information about your button interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Content | The type of content contained in the button. A button can contain a single text label or a group. For buttons containing a group, you can add text, images, and other objects to the group. |
| Title | The title string assigned to the interface controller. You can also set this value programmatically using the [`setTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/settitle(_:)) or [`setAttributedTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setattributedtitle(_:)) method. |
| Color (Button) | The color to apply to the button’s title. |
| Font | The font to apply to the button’s title. You can set font information programmatically using the [`setAttributedTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setattributedtitle(_:)) method. |
| Enabled | A checkbox indicating whether the button is enabled and sends events when tapped. You can also configure this value programmatically using the [`setEnabled(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setenabled(_:)) method. |
| Background | The background image to display in the button. You can also set this value programmatically using the [`setBackgroundImage(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:)), [`setBackgroundImageData(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:)), or [`setBackgroundImageNamed(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:)) method. |
| Color (Background) | The background color for the button. |

## Topics

### Setting the Button Title
- [func setTitle(String?)](settitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/settitle(_:)))
  Sets the button title to the specified string.
- [func setAttributedTitle(NSAttributedString?)](setattributedtitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setattributedtitle(_:)))
  Sets the button title to the specified attributed string.
### Setting the Button Background
- [func setBackgroundColor(UIColor?)](setbackgroundcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundcolor(_:)))
  Sets the background color of the button.
- [func setBackgroundImage(UIImage?)](setbackgroundimage(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimage(_:)))
  Sets the button’s background image to the specified image.
- [func setBackgroundImageData(Data?)](setbackgroundimagedata(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagedata(_:)))
  Sets the button’s background image to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](setbackgroundimagenamed(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setbackgroundimagenamed(_:)))
  Sets the button’s background image to the image in the named resource file.
### Enabling and Disabling the Button
- [func setEnabled(Bool)](setenabled(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/setenabled(_:)))
  Enables or disables the button.

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
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
  A button that you can use to trigger payments through Apple Pay.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)*