# WKAccessibilityIsVoiceOverRunning()

**Framework**: WatchKit  
**Kind**: func

Returns a Boolean value indicating whether VoiceOver is running.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func WKAccessibilityIsVoiceOverRunning() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if VoiceOver is currently running or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

You can use this function to customize your application’s UI specifically for VoiceOver users. For example, you might want UI elements that usually disappear quickly to persist onscreen for VoiceOver users. Note that you can also listen for the [`WKAccessibilityVoiceOverStatusChanged`](https://developer.apple.com/documentation/watchkit/wkaccessibilityvoiceoverstatuschanged) notification to find out when VoiceOver starts and stops.

## See Also

- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))
  Returns a Boolean value indicating whether reduced motion is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning())*