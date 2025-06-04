# WKAccessibilityImageRegion

**Framework**: Watchkit  
**Kind**: class

An object that defines a portion of an image that you want to call out separately to an assistive app.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKAccessibilityImageRegion
```

## Overview

The accessibility image region object defines the portion of the image that you want to call out separately and the label you want to apply to that region. Use an accessibility image region object in conjunction with any interface object that displays an image, either as part of its foreground or background content. Register your custom regions using the [`setAccessibilityImageRegions(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityimageregions(_:)) method of the corresponding interface object.

## Topics

### Getting the Region Attributes
- [var frame: CGRect](frame.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion/frame))
  A portion of the parent image, in the image’s coordinate system.
- [var label: String](label.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion/label))
  A succinct label that succinctly identifies the purpose of the image region.

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
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)*