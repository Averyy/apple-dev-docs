# WKAccessibilityIsReduceMotionEnabled()

**Framework**: WatchKit  
**Kind**: func

Returns a Boolean value indicating whether reduced motion is enabled.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
func WKAccessibilityIsReduceMotionEnabled() -> Bool
```

#### Discussion

You can use this function to customize your application’s UI when reduced motion is enabled. Note that you can also listen for the [`WKAccessibilityReduceMotionStatusDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/2915218-wkaccessibilityreducemotionstatu) (Swift) or [`WKAccessibilityReduceMotionStatusDidChangeNotification`](https://developer.apple.com/documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification) (Objective-C) notification to find out when VoiceOver starts and stops.

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
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
  Returns a Boolean value indicating whether VoiceOver is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled())*