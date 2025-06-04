# WKInterfaceDate

**Framework**: Watchkit  
**Kind**: class

A label that displays the current date or time.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceDate
```

## Overview

Use [`WKInterfaceDate`](https://developer.apple.com/documentation/watchkit/wkinterfacedate) when you want to display date or time information without further interaction from your WatchKit extension. At runtime, use the date object to configure the appearance of the date and time information being displayed.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a date object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed date objects and assigns them to their connected outlets. After those objects are set, you can use them to make changes to the onscreen date and time information.

Xcode lets you configure information about your date interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Attribute'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Description', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Format'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'A selector for choosing between standard and custom formats. For standard formats, you use the Date and Time attributes to configure the information you want to display. Changing the value of this attribute to Custom lets you configure the date exactly the way you want based on the format options described in ', 'type': 'text'}, {'identifier': 'https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i', 'isActive': True, 'type': 'reference'}, {'text': '.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Date'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The date information to display. The date options correspond to the values of the '}, {'type': 'reference', 'isActive': True, 'identifier': 'doc://com.apple.documentation/documentation/Foundation/DateFormatter/Style'}, {'type': 'text', 'text': ' type.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Time', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The time information to display. The time options correspond to the values of the ', 'type': 'text'}, {'identifier': 'doc://com.apple.documentation/documentation/Foundation/DateFormatter/Style', 'isActive': True, 'type': 'reference'}, {'text': ' type.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Preview', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'A preview of what the date and time will look like.', 'type': 'text'}], 'type': 'paragraph'}] |

A date object is a custom label whose text you cannot set directly. However, you can customize the appearance of the date object as you would customize a label using the Attributes inspector in Xcode. For information about the label attributes you can configure, see [`WKInterfaceLabel`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel).

## Topics

### Configuring the Date and Time Display
- [func setTextColor(UIColor?)](settextcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate/settextcolor(_:)))
  Sets the color of the date and time text.
- [func setTimeZone(TimeZone?)](settimezone(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate/settimezone(_:)))
  Sets the time zone to use when displaying time information.
- [func setCalendar(Calendar?)](setcalendar(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate/setcalendar(_:)))
  Sets the calendar to use when formatting date information.

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
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate)*