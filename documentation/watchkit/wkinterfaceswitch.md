# WKInterfaceSwitch

**Framework**: Watchkit  
**Kind**: class

An interface element that toggles between an On and Off state.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceSwitch
```

## Overview

Switches are commonly used to indicate whether a feature is enabled or disabled. You set the initial value of the switch in your storyboard file, but you can modify that value at runtime using the methods of this class.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a switch object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen switch.

When the user changes the value of a switch, WatchKit delivers the new value to the slider’s action method. The format of a switch’s action method is as follows:

Declare a method of this form in the interface controller class used to manage the switch. You can change the method name to anything you like. When configuring the switch in Xcode, connect its selector to your custom action method.

Xcode lets you configure information about switches in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Description'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'State', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The initial state of the switch. The switch can be off or on. You can modify the state of the switch programmatically at runtime using the ', 'type': 'text'}, {'type': 'reference', 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSwitch/setOn(_:)', 'isActive': True}, {'text': ' method.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Tint', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The color of the switch when it is in the on state.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Enabled', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'A checkbox indicating whether the switch is enabled. An enabled switch calls its action method when the user changes the state of the switch. You can enable or disable a switch programmatically using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSwitch/setEnabled(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Title', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The string to be displayed next to the switch. If specified, the title string is displayed next to the switch.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Color'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The text color for the switch’s title string. You can also set the switch color using the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceSwitch/setColor(_:)'}, {'type': 'text', 'text': ' method.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Font'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The font information to be applied to the title string. You can specify one of the predefined styles or provide custom style information.', 'type': 'text'}]}] |

## Topics

### Setting the Switch’s Title
- [func setTitle(String?)](settitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/settitle(_:)))
  Sets the switch title to the specified string.
- [func setAttributedTitle(NSAttributedString?)](setattributedtitle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setattributedtitle(_:)))
  Sets the switch title to the specified attributed string.
### Configuring the Switch
- [func setOn(Bool)](seton(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/seton(_:)))
  Sets the state of the switch to the specified value.
- [func setColor(UIColor?)](setcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setcolor(_:)))
  Changes the tint color of the switch when it is on.
### Enabling the Switch
- [func setEnabled(Bool)](setenabled(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setenabled(_:)))
  Enables or disables the switch.

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
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch)*