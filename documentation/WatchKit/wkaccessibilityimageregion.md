# WKAccessibilityImageRegion

**Framework**: WatchKit  
**Kind**: class  
**Role**: Class

An object that defines a portion of an image that you want to call out separately to an assistive app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAccessibilityImageRegion
```

```objc
@interface WKAccessibilityImageRegion : NSObject
```

#### Overview

The accessibility image region object defines the portion of the image that you want to call out separately and the label you want to apply to that region. Use an accessibility image region object in conjunction with any interface object that displays an image, either as part of its foreground or background content. Register your custom regions using the [`setAccessibilityImageRegions(_:)`](./wkinterfaceobject/setaccessibilityimageregions%28_%29.md) method of the corresponding interface object.

## Topics

### Getting the Region Attributes
- [var frame: CGRect](./wkaccessibilityimageregion/frame.md)
  A portion of the parent image, in the image’s coordinate system.
- [var label: String](./wkaccessibilityimageregion/label.md)
  A succinct label that succinctly identifies the purpose of the image region.

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
- [class WKAlertAction](./wkalertaction.md)
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](./wkaccessibilityisvoiceoverrunning%28%29.md)
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](./wkaccessibilityisreducemotionenabled%28%29.md)
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)*