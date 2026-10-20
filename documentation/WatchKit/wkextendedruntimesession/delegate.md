# delegate

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A delegate object for monitoring the session and responding to state changes and errors.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
weak var delegate: (any WKExtendedRuntimeSessionDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<WKExtendedRuntimeSessionDelegate> delegate;
```

#### Discussion

To receive all the delegate calls, always assign a value to this property before calling the session’s [`start()`](./start%28%29.md) or [`start(at:)`](./start%28at%29.md) methods.

## See Also

### Creating a Session
- [protocol WKExtendedRuntimeSessionDelegate](../wkextendedruntimesessiondelegate.md)
  A set of optional methods for monitoring an extended runtime session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/delegate)*