# isApplicationRunningInDock

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor var isApplicationRunningInDock: Bool { get }
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))

## Overview

This property contains [`true`](https://developer.apple.com/documentation/swift/true) if the app is running in the dock; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

Check this property (for example, in your extension delegate’s [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate))
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
- [var isFrontmostTimeoutExtended: Bool](isfrontmosttimeoutextended.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock)*