# start(at:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Schedules a session to start running at a future date.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func start(at date: Date)
```

```objc
- (void) startAtDate:(NSDate *) date;
```

## Mentions

- [Using extended runtime sessions](../using-extended-runtime-sessions.md)

## Discussion

Use [`start(at:)`](./start%28at%29.md) to set up a scheduable session. You must call this method while your app is running in the foreground. However, when the scheduled date and time arrives, the session starts running regardless of your app’s current state. If your app isn’t running, the system launches your app and calls your extension delegate’s [`handle(_:)`](../wkextensiondelegate/handle%28_%29-4qxgv.md) method to start the session. If you don’t set the session’s delegate in the [`handle(_:)`](../wkextensiondelegate/handle%28_%29-4qxgv.md) method, the system ends the session.

> ❗ **Important**:  You can only use this method for alarm sessions.

If you call this method with a date that has already passed, the system tries to immediately starts the session, but the session is only given 30 minutes from the provided date. If the date is more than one minute in the past, this method fails.

## Parameters

- `date`: The time and date when the session starts running.

## See Also

### Managing the Session State
- [func start()](./start%28%29.md)
  Starts running the session.
- [func invalidate()](./invalidate%28%29.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](./state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](../wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](./expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](./requestautolaunchauthorizationstatus%28completion%29.md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](../wkextendedruntimesessionautolaunchauthorizationstatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:))*