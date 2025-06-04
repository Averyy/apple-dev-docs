# WKAlertAction

**Framework**: WatchKit  
**Kind**: class

An object that encapsulates information about a button displayed in an alert or action sheet.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAlertAction
```

#### Overview

Create instances of this class using the [`init(title:style:handler:)`](https://developer.apple.com/documentation/watchkit/wkalertaction/init(title:style:handler:)) method and pass them to the [`presentAlert(withTitle:message:preferredStyle:actions:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)) method of one of your interface controllers. The sheet uses your action objects to create the corresponding buttons. When creating an alert action, you specify the title and visual style to apply to the button and a block to execute when the button is tapped. Use the defined visual styles to convey the purpose of the button to the user.

## Topics

### Creating an Action
- [convenience init(title: String, style: WKAlertActionStyle, handler: WKAlertActionHandler)](init(title:style:handler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction/init(title:style:handler:)))
  Creates and returns an action object with the specified button information.
### Constants
- [enum WKAlertActionStyle](wkalertactionstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertactionstyle))
  Constants indicating the style of the action button.
- [typealias WKAlertActionHandler](wkalertactionhandler.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertactionhandler))
  A block to perform in response to an action.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertaction)*