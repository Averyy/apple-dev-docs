# WKExtendedRuntimeSession

**Framework**: WatchKit  
**Kind**: class

A session that continues to run your app after the user has stopped interacting.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
class WKExtendedRuntimeSession
```

## Mentions

- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))
- [Using background tasks](using-background-tasks.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-background-tasks))

#### Overview

With extended runtime sessions, your app continues to run after the user stops interacting with it. The app can continue to communicate with Bluetooth devices, process data, or play sounds or haptics, even after the watch’s screen turns off.

Each app can support a single type of extended runtime session: self care, mindfulness, physical therapy, or smart alarm. Select the session by enabling the appropriate Background Modes capability.

For more information, see [`Using extended runtime sessions`](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions).

## Topics

### Creating a Session
- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](delegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/delegate))
  A delegate object for monitoring the session and responding to state changes and errors.
- [protocol WKExtendedRuntimeSessionDelegate](wkextendedruntimesessiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate))
  A set of optional methods for monitoring an extended runtime session.
### Managing the Session State
- [func start()](start().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()))
  Starts running the session.
- [func start(at: Date)](start(at:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)))
  Schedules a session to start running at a future date.
- [func invalidate()](invalidate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()))
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/state))
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionstate))
  The activation states for an extended runtime session.
- [var expirationDate: Date?](expirationdate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate))
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](requestautolaunchauthorizationstatus(completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:)))
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionautolaunchauthorizationstatus))
### Alerting the User
- [func notifyUser(hapticType: WKHapticType, repeatHandler: ((UnsafeMutablePointer<WKHapticType>) -> TimeInterval)?)](notifyuser(haptictype:repeathandler:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/notifyuser(haptictype:repeathandler:)))
  Play a repeating haptic alert.
### Handling Errors
- [enum WKExtendedRuntimeSessionErrorCode](wkextendedruntimesessionerrorcode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode))
  The error codes reported by extended runtime sessions.
- [let WKExtendedRuntimeSessionErrorDomain: String](wkextendedruntimesessionerrordomain.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrordomain))
  The domain for errors reported by extended runtime sessions.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Background execution](background-execution.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/background-execution))
  Manage background sessions and tasks.
- [Life cycles](life-cycles.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/life-cycles))
  Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh))
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession)*