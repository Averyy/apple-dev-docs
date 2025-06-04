# applicationDidEnterBackgroundNotification

**Framework**: Watchkit  
**Kind**: property

A message indicating that the watchOS app transitioned from the foreground to the background.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
class let applicationDidEnterBackgroundNotification: NSNotification.Name
```

## Overview

When creating an app that uses the SwiftUI [`App`](https://developer.apple.com/documentation/SwiftUI/App) protocol to manage your life cycle, use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier and the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value to monitor life cycle changes when possible. For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

## See Also

- [class let applicationDidFinishLaunchingNotification: NSNotification.Name](applicationdidfinishlaunchingnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidfinishlaunchingnotification))
- [class let applicationDidBecomeActiveNotification: NSNotification.Name](applicationdidbecomeactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidbecomeactivenotification))
- [class let applicationWillResignActiveNotification: NSNotification.Name](applicationwillresignactivenotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillresignactivenotification))
- [class let applicationWillEnterForegroundNotification: NSNotification.Name](applicationwillenterforegroundnotification.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationwillenterforegroundnotification))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationdidenterbackgroundnotification)*