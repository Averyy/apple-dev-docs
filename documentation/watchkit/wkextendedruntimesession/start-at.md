# start(at:)

**Framework**: Watchkit  
**Kind**: method

Schedules a session to start running at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func start(at date: Date)
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

## Overview

Use [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) to set up a scheduable session. You must call this method while your app is running in the foreground. However, when the scheduled date and time arrives, the session starts running regardless of your app’s current state. If your app isn’t running, the system launches your app and calls your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method to start the session. If you don’t set the session’s delegate in the [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method, the system ends the session.

> ❗ **Important**:  You can only use this method for alarm sessions.

 You can only use this method for alarm sessions.

If you call this method with a date that has already passed, the system tries to immediately starts the session, but the session is only given 30 minutes from the provided date. If the date is more than one minute in the past, this method fails.

## Parameters

- `date`: The time and date when the session starts running.

## See Also

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:))*