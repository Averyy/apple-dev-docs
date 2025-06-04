# WKExtendedRuntimeSessionState

**Framework**: Watchkit  
**Kind**: enum

The activation states for an extended runtime session.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionState
```

## Topics

### Session States
- [WKExtendedRuntimeSessionState.notStarted](notstarted.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/notstarted))
  The app has not yet started or scheduled the session.
- [WKExtendedRuntimeSessionState.scheduled](scheduled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/scheduled))
  The app has scheduled the session to run at a future date.
- [WKExtendedRuntimeSessionState.running](running.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/running))
  The session is actively running.
- [WKExtendedRuntimeSessionState.invalid](invalid.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/invalid))
  Either the session has encountered an error, or it has stopped running.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate)*