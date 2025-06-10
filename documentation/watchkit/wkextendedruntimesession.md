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

- [Using extended runtime sessions](using-extended-runtime-sessions.md)
- [Using background tasks](using-background-tasks.md)

#### Overview

With extended runtime sessions, your app continues to run after the user stops interacting with it. The app can continue to communicate with Bluetooth devices, process data, or play sounds or haptics, even after the watch’s screen turns off.

Each app can support a single type of extended runtime session: self care, mindfulness, physical therapy, or smart alarm. Select the session by enabling the appropriate Background Modes capability.

For more information, see [`Using extended runtime sessions`](using-extended-runtime-sessions.md).

## Topics

### Creating a Session
- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](wkextendedruntimesession/delegate.md)
  A delegate object for monitoring the session and responding to state changes and errors.
- [protocol WKExtendedRuntimeSessionDelegate](wkextendedruntimesessiondelegate.md)
  A set of optional methods for monitoring an extended runtime session.
### Managing the Session State
- [func start()](wkextendedruntimesession/start.md)
  Starts running the session.
- [func start(at: Date)](wkextendedruntimesession/start(at:).md)
  Schedules a session to start running at a future date.
- [func invalidate()](wkextendedruntimesession/invalidate.md)
  Stops the session.
- [var state: WKExtendedRuntimeSessionState](wkextendedruntimesession/state.md)
  The session’s current state.
- [enum WKExtendedRuntimeSessionState](wkextendedruntimesessionstate.md)
  The activation states for an extended runtime session.
- [var expirationDate: Date?](wkextendedruntimesession/expirationdate.md)
  The time and date when the session expires.
- [class func requestAutoLaunchAuthorizationStatus(completion: (WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus, (any Error)?) -> Void)](wkextendedruntimesession/requestautolaunchauthorizationstatus(completion:).md)
- [enum WKExtendedRuntimeSessionAutoLaunchAuthorizationStatus](wkextendedruntimesessionautolaunchauthorizationstatus.md)
### Alerting the User
- [func notifyUser(hapticType: WKHapticType, repeatHandler: ((UnsafeMutablePointer<WKHapticType>) -> TimeInterval)?)](wkextendedruntimesession/notifyuser(haptictype:repeathandler:).md)
  Play a repeating haptic alert.
### Handling Errors
- [enum WKExtendedRuntimeSessionErrorCode](wkextendedruntimesessionerrorcode.md)
  The error codes reported by extended runtime sessions.
- [let WKExtendedRuntimeSessionErrorDomain: String](wkextendedruntimesessionerrordomain.md)
  The domain for errors reported by extended runtime sessions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Background execution](background-execution.md)
  Manage background sessions and tasks.
- [Life cycles](life-cycles.md)
  Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](using-extended-runtime-sessions.md)
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md)
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession)*