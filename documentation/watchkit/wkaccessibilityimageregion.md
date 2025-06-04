# WKAccessibilityImageRegion

**Framework**: WatchKit  
**Kind**: class

An object that defines a portion of an image that you want to call out separately to an assistive app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAccessibilityImageRegion
```

#### Overview

The accessibility image region object defines the portion of the image that you want to call out separately and the label you want to apply to that region. Use an accessibility image region object in conjunction with any interface object that displays an image, either as part of its foreground or background content. Register your custom regions using the [`setAccessibilityImageRegions(_:)`](wkinterfaceobject/setaccessibilityimageregions(_:).md) method of the corresponding interface object.

## Topics

### Getting the Region Attributes
- [var frame: CGRect](wkaccessibilityimageregion/frame.md)
  A portion of the parent image, in the image’s coordinate system.
- [var label: String](wkaccessibilityimageregion/label.md)
  A succinct label that succinctly identifies the purpose of the image region.

## Relationships

### Inherits From
- [NSObject](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class)
### Conforms To
- [CVarArg](https://developer.apple.com/documentation/Swift/CVarArg)
- [CustomDebugStringConvertible](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible)
- [CustomStringConvertible](https://developer.apple.com/documentation/Swift/CustomStringConvertible)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [NSObjectProtocol](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol)

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md)
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md)
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md)
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAlertAction](wkalertaction.md)
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)*