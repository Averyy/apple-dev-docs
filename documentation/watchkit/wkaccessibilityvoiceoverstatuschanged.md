# WKAccessibilityVoiceOverStatusChanged

**Framework**: Watchkit  
**Kind**: var

Tells the interface controller that the VoiceOver status has changed.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
let WKAccessibilityVoiceOverStatusChanged: String
```

#### Discussion

Use this notification to customize your application’s user interface for VoiceOver users. You can also use the [`isVoiceOverRunning`](https://developer.apple.com/documentation/UIKit/UIAccessibility/isVoiceOverRunning) function to determine whether VoiceOver is currently running.

Observe this notification using the default notification center. This notification doesn’t include a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaccessibilityvoiceoverstatuschanged)*