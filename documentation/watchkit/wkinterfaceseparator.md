# WKInterfaceSeparator

**Framework**: WatchKit  
**Kind**: class

An interface object that displays a visual separator within a group.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceSeparator
```

#### Overview

Use [`WKInterfaceSeparator`](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator) to manipulate a separator at runtime, such as changing its color. You can also use the inherited methods to show or hide it and configure other attributes.

Do not subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a separator object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates any needed separator objects and assigns them to their connected outlets. At that point, you can use those objects to make changes to the onscreen text.

##### Interface Builder Configuration Options

Xcode lets you configure information about your separator interface object in your storyboard file. The following table lists the attributes you can configure and their meaning.

| Attribute | Description |
| --- | --- |
| Color | The default color of the separator. You can also set this value programmatically using the [`setColor(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator/setcolor(_:)) method. |

## Topics

### Configuring the Separator
- [func setColor(UIColor?)](setcolor(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator/setcolor(_:)))
  Sets the color of the separator bar.

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

- [class WKInterfaceGroup](wkinterfacegroup.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup))
  A container for one or more interface objects.
- [class WKInterfaceTable](wkinterfacetable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable))
  An object that creates and manages the contents of a single-column table interface.
- [class WKInterfacePicker](wkinterfacepicker.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker))
  An interface element that presents a scrolling list of items for the user to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator)*