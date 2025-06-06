# WKAlertAction

**Framework**: Watchkit  
**Kind**: class

An object that encapsulates information about a button displayed in an alert or action sheet.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAlertAction
```

#### Overview

Create instances of this class using the [`init(title:style:handler:)`](wkalertaction/init(title:style:handler:).md) method and pass them to the [`presentAlert(withTitle:message:preferredStyle:actions:)`](wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:).md) method of one of your interface controllers. The sheet uses your action objects to create the corresponding buttons. When creating an alert action, you specify the title and visual style to apply to the button and a block to execute when the button is tapped. Use the defined visual styles to convey the purpose of the button to the user.

## Topics

### Creating an Action
- [convenience init(title: String, style: WKAlertActionStyle, handler: WKAlertActionHandler)](wkalertaction/init(title:style:handler:).md)
  Creates and returns an action object with the specified button information.
### Constants
- [enum WKAlertActionStyle](wkalertactionstyle.md)
  Constants indicating the style of the action button.
- [typealias WKAlertActionHandler](wkalertactionhandler.md)
  A block to perform in response to an action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md)
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md)
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md)
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md)
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertaction)*