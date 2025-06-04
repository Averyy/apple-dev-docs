# isApplicationRunningInDock

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates whether the app is running in the dock.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor var isApplicationRunningInDock: Bool { get }
```

## Overview

This property contains [`true`](https://developer.apple.com/documentation/swift/true) if the app is running in the dock; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

Check this property (for example, in your app delegate’s [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()) method) to determine whether your app is running in the dock. You can use this information to customize your user interface in the dock.

## See Also

- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/applicationstate))
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isapplicationrunningindock)*