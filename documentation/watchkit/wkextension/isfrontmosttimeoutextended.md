# isFrontmostTimeoutExtended

**Framework**: WatchKit  
**Kind**: property

A Boolean value that determines whether the app extends its time as the frontmost app.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
var isFrontmostTimeoutExtended: Bool { get set }
```

## Mentions

- [Taking Advantage of Frontmost App State](taking-advantage-of-frontmost-app-state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/taking-advantage-of-frontmost-app-state))

#### Discussion

This value defaults to [`false`](https://developer.apple.com/documentation/swift/false). An app remains the frontmost app for two minutes after the user drops their wrist. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) extends the app’s time as the frontmost app to eight minutes.

Don’t just extend the app’s frontmost time globally. Instead, enable it only when the user performs an activity that they are likely to continue. Otherwise, disable it. Users can also change the default length of time that apps spend as the frontmost app by choosing Settings > General > Wake Screen. If they select a time that is eight minutes or longer, this property has no effect. In other words, when [`isFrontmostTimeoutExtended`](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended) is [`true`](https://developer.apple.com/documentation/swift/true), the app remains the frontmost app for eight minutes, or for the amount of time that the user selects, whichever is longer.

## See Also

- [var applicationState: WKApplicationState](applicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate))
  The runtime state of the Watch app.
- [enum WKApplicationState](wkapplicationstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate))
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](isapplicationrunningindock.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock))
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/schedulebackgroundrefresh(withpreferreddate:userinfo:scheduledcompletion:)))
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended)*