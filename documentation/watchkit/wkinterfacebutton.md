# WKInterfaceButton

**Framework**: Watchkit  
**Kind**: class

A button in the user interface of your watchOS app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceButton
```

## Overview

The content of a button’s tappable area is filled with text and an optional background color or image. When tapped by the user, the button calls its associated action method, which you define on the owning interface controller. Use that action method to initiate tasks and update your app’s interface.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a button object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen button.

To respond to taps in the button, declare a method of this form in the interface controller class that manages the button:

You can change the name of your action method to anything you like. In your Xcode storyboard, connect the button’s selector to the custom action method defined in your class.

Xcode lets you configure information about your button interface object in your storyboard file. The following table lists the attributes you can configure in your storyboard and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Attribute', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Content'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The type of content contained in the button. A button can contain a single text label or a group. For buttons containing a group, you can add text, images, and other objects to the group.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Title'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The title string assigned to the interface controller. You can also set this value programmatically using the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setTitle(_:)'}, {'type': 'text', 'text': ' or '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setAttributedTitle(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Color (Button)', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The color to apply to the button’s title.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Font', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The font to apply to the button’s title. You can set font information programmatically using the ', 'type': 'text'}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setAttributedTitle(_:)', 'isActive': True, 'type': 'reference'}, {'text': ' method.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Enabled'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'A checkbox indicating whether the button is enabled and sends events when tapped. You can also configure this value programmatically using the ', 'type': 'text'}, {'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setEnabled(_:)', 'type': 'reference'}, {'text': ' method.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Background', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The background image to display in the button. You can also set this value programmatically using the '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setBackgroundImage(_:)'}, {'type': 'text', 'text': ', '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setBackgroundImageData(_:)'}, {'type': 'text', 'text': ', or '}, {'isActive': True, 'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceButton/setBackgroundImageNamed(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Color (Background)', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The background color for the button.', 'type': 'text'}]}] |

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
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)*