# WKAccessibilityVoiceOverStatusChanged

**Framework**: WatchKit  
**Kind**: var  
**Role**: Global Variable

Tells the interface controller that the VoiceOver status has changed.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
let WKAccessibilityVoiceOverStatusChanged: String
```

```c
extern NSString * const WKAccessibilityVoiceOverStatusChanged;
```

## Discussion

Use this notification to customize your application’s user interface for VoiceOver users. You can also use the [`isVoiceOverRunning`](../UIKit/uiaccessibility/isvoiceoverrunning.md) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### Managing Notifications
- [WKAccessibilityReduceMotionStatusDidChangeNotification](./wkaccessibilityreducemotionstatusdidchangenotification.md)
  Tells the interface controller that the reduce motion status has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityvoiceoverstatuschanged)*