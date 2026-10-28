# WKAccessibilityReduceMotionStatusDidChangeNotification

**Framework**: WatchKit  
**Kind**: var  
**Role**: Global Variable

Tells the interface controller that the reduce motion status has changed.

**Availability**:
- watchOS 4.0+

## Declaration

```c
extern NSString * const WKAccessibilityReduceMotionStatusDidChangeNotification;
```

## Discussion

Use this notification to customize your application’s user interface for when reduced motion is enabled. You can also use the [`WKAccessibilityIsReduceMotionEnabled()`](./wkaccessibilityisreducemotionenabled%28%29.md) function to determine whether reduced motion is enabled.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### Managing Notifications
- [let WKAccessibilityVoiceOverStatusChanged: String](./wkaccessibilityvoiceoverstatuschanged.md)
  Tells the interface controller that the VoiceOver status has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification)*