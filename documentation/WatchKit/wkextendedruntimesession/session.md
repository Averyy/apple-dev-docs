# session

**Framework**: WatchKit  
**Kind**: method  
**Role**: Type Method

Instantiates a new session object.

**Availability**:
- watchOS 6.0+

## Declaration

```objc
+ (WKExtendedRuntimeSession *) session;
```

## Discussion

The system sets the session’s type based on the Session Type setting in your WatchKit Extension’s Background Modes capability. For more information, see [Set Up the Session](../using-extended-runtime-sessions.md#Set-Up-the-Session).

## See Also

### Creating a Session
- [var delegate: (any WKExtendedRuntimeSessionDelegate)?](./delegate.md)
  A delegate object for monitoring the session and responding to state changes and errors.
- [protocol WKExtendedRuntimeSessionDelegate](../wkextendedruntimesessiondelegate.md)
  A set of optional methods for monitoring an extended runtime session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/session)*