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

#### Overview

Use [`WKInterfaceDate`](wkinterfacedate.md) when you want to display date or time information without further interaction from your WatchKit extension. At runtime, use the date object to configure the appearance of the date and time information being displayed.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a date object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed date objects and assigns them to their connected outlets. After those objects are set, you can use them to make changes to the onscreen date and time information.

##### Interface Builder Configuration Options

Xcode lets you configure information about your date interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Format | A selector for choosing between standard and custom formats. For standard formats, you use the Date and Time attributes to configure the information you want to display. Changing the value of this attribute to Custom lets you configure the date exactly the way you want based on the format options described in [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i). |
| Date | The date information to display. The date options correspond to the values of the [`DateFormatter.Style`](https://developer.apple.com/documentation/Foundation/DateFormatter/Style) type. |
| Time | The time information to display. The time options correspond to the values of the [`DateFormatter.Style`](https://developer.apple.com/documentation/Foundation/DateFormatter/Style) type. |
| Preview | A preview of what the date and time will look like. |

A date object is a custom label whose text you cannot set directly. However, you can customize the appearance of the date object as you would customize a label using the Attributes inspector in Xcode. For information about the label attributes you can configure, see [`WKInterfaceLabel`](wkinterfacelabel.md).

## Topics

### Configuring the Date and Time Display
- [func setTextColor(UIColor?)](wkinterfacedate/settextcolor(_:).md)
  Sets the color of the date and time text.
- [func setTimeZone(TimeZone?)](wkinterfacedate/settimezone(_:).md)
  Sets the time zone to use when displaying time information.
- [func setCalendar(Calendar?)](wkinterfacedate/setcalendar(_:).md)
  Sets the calendar to use when formatting date information.

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
- [class WKInterfaceTimer](wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md)
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedate)*