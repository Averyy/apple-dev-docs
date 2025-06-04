# WKInterfaceTimer

**Framework**: Watchkit  
**Kind**: class

A label that displays a countdown or count-up timer.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceTimer
```

## Overview

Use a timer object to configure the amount of time and the appearance of the timer text. When you start the timer, WatchKit updates the displayed text automatically on the user’s Apple Watch without further interactions from your extension. To know when the timer reaches 0, configure a [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) object with the same target date you used to set up the timer.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a timer object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed timer objects and assigns them to their connected outlets. At that point, you can use those objects to reconfigure the corresponding timers.

> ❗ **Important**:  This class provides methods for configuring interface objects at initialization time or while an interface controller is active on the user’s Apple Watch. WatchKit coalesces the data from all setter method calls made during the same run loop iteration and transmits it to the device at the end of the run loop. If you set an attribute to different values in the same run loop iteration,  only the last value is transmitted. If you set an attribute to the same value in the same run loop iteration, WatchKit generates a log message so that you can track down the duplicate change.

 This class provides methods for configuring interface objects at initialization time or while an interface controller is active on the user’s Apple Watch. WatchKit coalesces the data from all setter method calls made during the same run loop iteration and transmits it to the device at the end of the run loop. If you set an attribute to different values in the same run loop iteration,  only the last value is transmitted. If you set an attribute to the same value in the same run loop iteration, WatchKit generates a log message so that you can track down the duplicate change.

Xcode lets you configure information about your timer interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Attribute'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Description', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Format', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The format of the timer string. Select different options to update the appearance of the timer label in your storyboard scene.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Enabled', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'A checkbox indicating whether the timer starts running as soon as your interface is initialized.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Units', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The units to be displayed in the label. Enabling checkboxes in this section causes the timer to display the corresponding units that are in range of the time. In other words, a timer with 2 minutes remaining displays minutes and seconds only; it does not display hours, days, or any larger units.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Preview Secs', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The initial number of seconds for the timer. You can change this value programmatically using the '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKInterfaceTimer/setDate(_:)', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' method.'}]}] |

A date object is a custom label whose text you cannot set directly. However, you can customize the appearance of the date object as you would for a label using the Attributes inspector in Xcode. For information about the label attributes you can configure, see [`WKInterfaceLabel`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel).

## Topics

### Configuring the Timer Attributes
- [func setDate(Date)](setdate(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/setdate(_:)))
  Changes the start time for the timer.
- [func setTextColor(UIColor?)](settextcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/settextcolor(_:)))
  Sets the color of the timer’s text.
### Starting and Stopping the Timer
- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/start()))
  Begins updates to the timer’s display.
- [func stop()](stop().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/stop()))
  Stops updates to the timer’s display.

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
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer)*