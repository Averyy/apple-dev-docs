# isFrontmostTimeoutExtended

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the app extends its time as the frontmost app.

**Availability**:
- watchOS 4.0+ - Deprecated in 7.0

> **Deprecated**: In watchOS 7 and later, you can no longer request extended frontmost time. Instead, the user can set the frontmost app behavior for each app using its Return to App setting.

## Declaration

```swift
var isFrontmostTimeoutExtended: Bool { get set }
```

```objc
@property (nonatomic, getter=isFrontmostTimeoutExtended) BOOL frontmostTimeoutExtended;
```

## Mentions

- [Taking advantage of frontmost app state](../taking-advantage-of-frontmost-app-state.md)

## Discussion

This value defaults to [`false`](../../Swift/false.md). An app remains the frontmost app for two minutes after the user drops their wrist. Setting this property to [`true`](../../Swift/true.md) extends the app’s time as the frontmost app to eight minutes.

Don’t just extend the app’s frontmost time globally. Instead, enable it only when the user performs an activity that they are likely to continue. Otherwise, disable it. Users can also change the default length of time that apps spend as the frontmost app by choosing Settings > General > Wake Screen. If they select a time that is eight minutes or longer, this property has no effect. In other words, when [`isFrontmostTimeoutExtended`](./isfrontmosttimeoutextended.md) is [`true`](../../Swift/true.md), the app remains the frontmost app for eight minutes, or for the amount of time that the user selects, whichever is longer.

## See Also

### Managing the execution state
- [var applicationState: WKApplicationState](./applicationstate.md)
  The runtime state of the Watch app.
- [enum WKApplicationState](../wkapplicationstate.md)
  The running states of the Watch app.
- [var isApplicationRunningInDock: Bool](./isapplicationrunningindock.md)
  A Boolean value that indicates whether the app is running in the dock.
- [func scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: (any NSSecureCoding & NSObjectProtocol)?, scheduledCompletion: ((any Error)?) -> Void)](./schedulebackgroundrefresh%28withpreferreddate,userinfo,scheduledcompletion%29.md)
  Schedules a background task to refresh the app’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isfrontmosttimeoutextended)*