# start()

**Framework**: Watchkit  
**Kind**: method

Starts running the session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func start()
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

## Overview

Use [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) to begin a session. You must call this method while your app is running in the foreground.

You can’t use the [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()) method to set up a schedulable session (such as a smart alarm session). Call the [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) method instead.

## See Also

- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start())*