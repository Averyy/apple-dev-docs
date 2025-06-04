# notifyUser(hapticType:repeatHandler:)

**Framework**: WatchKit  
**Kind**: method

Play a repeating haptic alert.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func notifyUser(hapticType type: WKHapticType, repeatHandler: ((UnsafeMutablePointer<WKHapticType>) -> TimeInterval)? = nil)
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

#### Discussion

For schedulable sessions such as smart alarms, call this method during the session to alert the user. When you call the method, the system plays repeating haptic feedback. If the app isn’t active, the system also displays a system alarm alert on the watch.

The haptic feedback repeats at the interval specified by the `repeatHandler`, and continues to repeat until the application or system alert invalidates the session.

- If the app isn’t active, the user can tap the Stop button to invalidate the session or tap the Open button to activate the app.
- If the app is active, the app must invalidate the session by calling its [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) method.

Only call this method on a schedulable session that’s running: you must schedule the session using the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method, and the session’s state must equal [`WKExtendedRuntimeSessionState.running`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running). During a smart alarm session, your app must call this method before the session expires.

## Parameters

- `type`: The type of haptic to play. For a complete list of haptic types, see  .
- `repeatHandler`: Use this block to change the haptic type by modifying the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/notifyuser(haptictype:repeathandler:))*