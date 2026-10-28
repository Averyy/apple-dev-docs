# WKExtendedRuntimeSessionErrorCode

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

The error codes reported by extended runtime sessions.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
enum WKExtendedRuntimeSessionErrorCode
```

```c
enum WKExtendedRuntimeSessionErrorCode : NSInteger;
```

## Overview

The session passes these errors to the sesson delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](./wkextendedruntimesessiondelegate/extendedruntimesession%28_,didinvalidatewith,error%29.md) method.

## Topics

### Error Codes
- [WKExtendedRuntimeSessionErrorCode.unknown](./wkextendedruntimesessionerrorcode/unknown.md)
  An unknown error occurred.
- [WKExtendedRuntimeSessionErrorCode.scheduledTooFarInAdvance](./wkextendedruntimesessionerrorcode/scheduledtoofarinadvance.md)
  The app attempted to schedule a session too far in the future.
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToStartOrSchedule](./wkextendedruntimesessionerrorcode/mustbeactivetostartorschedule.md)
  The watchOS app attempted to start or schedule a session while not in an active state.
- [WKExtendedRuntimeSessionErrorCode.notYetStarted](./wkextendedruntimesessionerrorcode/notyetstarted.md)
  The app invalidated the session before it started.
- [WKExtendedRuntimeSessionErrorCode.exceededResourceLimits](./wkextendedruntimesessionerrorcode/exceededresourcelimits.md)
  The session exceeded its resource limits.
- [WKExtendedRuntimeSessionErrorCode.barDisabled](./wkextendedruntimesessionerrorcode/bardisabled.md)
  The user has disabled background app refresh.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToStartSession](./wkextendedruntimesessionerrorcode/notapprovedtostartsession.md)
  The app attempted to start a session, but doesn’t have a valid session type.
- [WKExtendedRuntimeSessionErrorCode.notApprovedToSchedule](./wkextendedruntimesessionerrorcode/notapprovedtoschedule.md)
  The app attempted to schedule a session, but the session type does not support scheduling.
### Enumeration Cases
- [WKExtendedRuntimeSessionErrorCode.mustBeActiveToPrompt](./wkextendedruntimesessionerrorcode/mustbeactivetoprompt.md)
- [WKExtendedRuntimeSessionErrorCode.unsupportedSessionType](./wkextendedruntimesessionerrorcode/unsupportedsessiontype.md)
### Initializers
- [init?(rawValue: Int)](./wkextendedruntimesessionerrorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling Errors
- [let WKExtendedRuntimeSessionErrorDomain: String](./wkextendedruntimesessionerrordomain.md)
  The domain for errors reported by extended runtime sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode)*