# willResignActiveNotification

**Framework**: Watchkit  
**Kind**: property

A message indicating that the system is about to deactivate the watchOS app.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor @preconcurrency static let willResignActiveNotification: NSNotification.Name
```

## Overview

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [static let didFinishLaunchingNotification: NSNotification.Name](didfinishlaunchingnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didfinishlaunchingnotification))
- [static let didBecomeActiveNotification: NSNotification.Name](didbecomeactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didbecomeactivenotification))
- [static let willEnterForegroundNotification: NSNotification.Name](willenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/willenterforegroundnotification))
- [static let didEnterBackgroundNotification: NSNotification.Name](didenterbackgroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didenterbackgroundnotification))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/willresignactivenotification)*