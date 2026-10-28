# WKInterfaceButton

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

A button in the user interface of your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceButton
```

```objc
@interface WKInterfaceButton : WKInterfaceObject
```

## Overview

The content of a button’s tappable area is filled with text and an optional background color or image. When tapped by the user, the button calls its associated action method, which you define on the owning interface controller. Use that action method to initiate tasks and update your app’s interface.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a button object in your interface, define a property with the following syntax in your interface controller class:

**Swift**:

```swift
@IBOutlet weak var myButton: WKInterfaceButton!
```

**Objective-C**:

```objc
@property (weak, nonatomic) IBOutlet WKInterfaceButton* myButton;
```

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen button.

To respond to taps in the button, declare a method of this form in the interface controller class that manages the button:

**Swift**:

```swift
@IBAction func buttonAction()
```

**Objective-C**:

```objc
- (IBAction)buttonAction
```

You can change the name of your action method to anything you like. In your Xcode storyboard, connect the button’s selector to the custom action method defined in your class.

### Interface Builder Configuration Options

Xcode lets you configure information about your button interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| Attribute | Description |
| --- | --- |
| Content | The type of content contained in the button. A button can contain a single text label or a group. For buttons containing a group, you can add text, images, and other objects to the group. |
| Title | The title string assigned to the interface controller. You can also set this value programmatically using the [`setTitle(_:)`](./wkinterfacebutton/settitle%28_%29.md) or [`setAttributedTitle(_:)`](./wkinterfacebutton/setattributedtitle%28_%29.md) method. |
| Color (Button) | The color to apply to the button’s title. |
| Font | The font to apply to the button’s title. You can set font information programmatically using the [`setAttributedTitle(_:)`](./wkinterfacebutton/setattributedtitle%28_%29.md) method. |
| Enabled | A checkbox indicating whether the button is enabled and sends events when tapped. You can also configure this value programmatically using the [`setEnabled(_:)`](./wkinterfacebutton/setenabled%28_%29.md) method. |
| Background | The background image to display in the button. You can also set this value programmatically using the [`setBackgroundImage(_:)`](./wkinterfacebutton/setbackgroundimage%28_%29.md), [`setBackgroundImageData(_:)`](./wkinterfacebutton/setbackgroundimagedata%28_%29.md), or [`setBackgroundImageNamed(_:)`](./wkinterfacebutton/setbackgroundimagenamed%28_%29.md) method. |
| Color (Background) | The background color for the button. |

## Topics

### Setting the Button Title
- [func setTitle(String?)](./wkinterfacebutton/settitle%28_%29.md)
  Sets the button title to the specified string.
- [func setAttributedTitle(NSAttributedString?)](./wkinterfacebutton/setattributedtitle%28_%29.md)
  Sets the button title to the specified attributed string.
### Setting the Button Background
- [func setBackgroundColor(UIColor?)](./wkinterfacebutton/setbackgroundcolor%28_%29.md)
  Sets the background color of the button.
- [func setBackgroundImage(UIImage?)](./wkinterfacebutton/setbackgroundimage%28_%29.md)
  Sets the button’s background image to the specified image.
- [func setBackgroundImageData(Data?)](./wkinterfacebutton/setbackgroundimagedata%28_%29.md)
  Sets the button’s background image to the image in the specified data object.
- [func setBackgroundImageNamed(String?)](./wkinterfacebutton/setbackgroundimagenamed%28_%29.md)
  Sets the button’s background image to the image in the named resource file.
### Enabling and Disabling the Button
- [func setEnabled(Bool)](./wkinterfacebutton/setenabled%28_%29.md)
  Enables or disables the button.

## Relationships

### Inherits From
- [WKInterfaceObject](./wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Controls
- [class WKInterfaceLabel](./wkinterfacelabel.md)
  An interface element that displays static text.
- [class WKInterfaceDate](./wkinterfacedate.md)
  A label that displays the current date or time.
- [class WKInterfaceTimer](./wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceAuthorizationAppleIDButton](./wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](./wkinterfacepaymentbutton.md)
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](./wkinterfacetextfield.md)
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](./wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](./wkinterfaceslider.md)
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](./wkinterfaceactivityring.md)
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](./wkinterfacemap.md)
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)*