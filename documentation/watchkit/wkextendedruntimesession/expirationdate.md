# expirationDate

**Framework**: Watchkit  
**Kind**: property

The time and date when the session expires.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
var expirationDate: Date? { get }
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))

## Overview

Use this property to determine how much time remains before the session stops running.

This property starts set to `nil`. The system assigns a date as soon as the session starts running. This property remains valid, even after the session becomes invalid.

## See Also

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate)*