# WKAlertAction

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

An object that encapsulates information about a button displayed in an alert or action sheet.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAlertAction
```

```objc
@interface WKAlertAction : NSObject
```

## Overview

Create instances of this class using the [`init(title:style:handler:)`](./wkalertaction/init%28title,style,handler%29.md) method and pass them to the [`presentAlert(withTitle:message:preferredStyle:actions:)`](./wkinterfacecontroller/presentalert%28withtitle,message,preferredstyle,actions%29.md) method of one of your interface controllers. The sheet uses your action objects to create the corresponding buttons. When creating an alert action, you specify the title and visual style to apply to the button and a block to execute when the button is tapped. Use the defined visual styles to convey the purpose of the button to the user.

## Topics

### Creating an Action
- [convenience init(title: String, style: WKAlertActionStyle, handler: WKAlertActionHandler)](./wkalertaction/init%28title,style,handler%29.md)
  Creates and returns an action object with the specified button information.
### Constants
- [enum WKAlertActionStyle](./wkalertactionstyle.md)
  Constants indicating the style of the action button.
- [typealias WKAlertActionHandler](./wkalertactionhandler.md)
  A block to perform in response to an action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### User interface basics
- [Building watchOS app Interfaces Using the Storyboard](./building-watchos-app-interfaces-using-the-storyboard.md)
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](./wkinterfaceobject.md)
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](./wkinterfacecontroller.md)
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAccessibilityImageRegion](./wkaccessibilityimageregion.md)
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](./wkaccessibilityisvoiceoverrunning%28%29.md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](./wkaccessibilityisreducemotionenabled%28%29.md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertaction)*