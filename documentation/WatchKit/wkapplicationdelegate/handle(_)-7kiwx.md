# handle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the system launched your app to resume an extended runtime session.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
optional func handle(_ extendedRuntimeSession: WKExtendedRuntimeSession)
```

```objc
- (void) handleExtendedRuntimeSession:(WKExtendedRuntimeSession *) extendedRuntimeSession;
```

#### Discussion

The system calls this method after launching your app in response to a scheduled extended runtime session. This occurs if your app terminates after scheduling a session but before that session’s start date. The system may also call this method if your app crashes during an extended runtime session, letting you resume that session.

When implementing this method, set the session’s delegate to resume the session. If you don’t set the session’s delegate, the system ends the session.

## Parameters

- `extendedRuntimeSession`: The extended runtime session that the system is resuming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/handle(_:)-7kiwx)*