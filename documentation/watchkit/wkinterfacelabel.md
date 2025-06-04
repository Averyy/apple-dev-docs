# WKInterfaceLabel

**Framework**: WatchKit  
**Kind**: class

An interface element that displays static text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceLabel
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))

#### Overview

Use [`WKInterfaceLabel`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel) to manipulate the contents of a label at runtime, such as setting a new text string. The string you specify can use the default styling you specified at design time, or you can use an attributed string to add custom styling to the text.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a label object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed label objects and assigns them to their connected outlets. At that point, you can use those objects to make changes to the onscreen text.

Label objects apply the font and style information specified in your storyboard. You can specify a different set of style attributes by calling the [`setAttributedText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)) method and providing an appropriately formatted attributed string object. When specifying text with an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object, the only other change you can make is to the text color.

##### Interface Builder Configuration Options

Xcode lets you configure information about your label interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Text | The initial text to be displayed. You can change this value programmatically using the [`setText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settext(_:)) or [`setAttributedText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)) method. |
| Text Color | The default color of the text. You can also set this value programmatically using the [`setTextColor(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:)) method. |
| Font | The font information to be applied to the text. You can specify one of the predefined styles or provide custom style information. For custom fonts, you must include the font in your WatchKit app bundle. You can also apply font information when using the [`setAttributedText(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)) method. |
| Min Scale | The amount by which the font may be scaled to accommodate text. Values must be `1.0` or less. Specifying a value of `0` causes WatchKit to use the default scaling behavior, which allows scaling to `0.8` of the original font size. |
| Baseline | The technique for adjusting the position of the label’s text. When centering text vertically, you can center the text relative to the baseline or to the center of the label’s bounding box. |
| Alignment | The alignment of the text within its bounding rectangle. Use this attribute to align text when the width of the label is greater than the width of the text itself. |
| Lines | The maximum number of lines to allow for the label text. Text that does not fit on the specified number of lines is truncated. |

## Topics

### Setting the Label Text
- [func setText(String?)](settext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settext(_:)))
  Sets the label text to the specified string.
- [func setTextColor(UIColor?)](settextcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/settextcolor(_:)))
  Sets the color to apply to plain text strings.
- [func setAttributedText(NSAttributedString?)](setattributedtext(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel/setattributedtext(_:)))
  Sets the label text to the specified attributed string.

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

- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
  A button in the user interface of your watchOS app.
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

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacelabel)*