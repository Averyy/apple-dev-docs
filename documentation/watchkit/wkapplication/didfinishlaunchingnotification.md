# didFinishLaunchingNotification

**Framework**: Watchkit  
**Kind**: property

A message indicating that the launch process finished and the extension is ready to run.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor @preconcurrency static let didFinishLaunchingNotification: NSNotification.Name
```

## Overview

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [static let didBecomeActiveNotification: NSNotification.Name](didbecomeactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didbecomeactivenotification))
- [static let willResignActiveNotification: NSNotification.Name](willresignactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/willresignactivenotification))
- [static let willEnterForegroundNotification: NSNotification.Name](willenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/willenterforegroundnotification))
- [static let didEnterBackgroundNotification: NSNotification.Name](didenterbackgroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/didenterbackgroundnotification))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/didfinishlaunchingnotification)*