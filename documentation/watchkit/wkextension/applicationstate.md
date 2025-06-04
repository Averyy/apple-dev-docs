# applicationState

**Framework**: Watchkit  
**Kind**: property

The runtime state of the Watch app.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
@MainActor var applicationState: WKApplicationState { get }
```

## Overview

The Watch app may be active, inactive, or running in the background. Use this property to get the current state. To be notified of state changes, implement the appropriate methods of the [`delegate`](https://developer.apple.com/documentation/watchkit/wkextension/delegate) object.

## See Also

- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock))
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
- [var isFrontmostTimeoutExtended: Bool](isfrontmosttimeoutextended.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate)*