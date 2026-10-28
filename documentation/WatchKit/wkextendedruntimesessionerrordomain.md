# WKExtendedRuntimeSessionErrorDomain

**Framework**: WatchKit  
**Kind**: var  
**Role**: Global Variable

The domain for errors reported by extended runtime sessions.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
let WKExtendedRuntimeSessionErrorDomain: String
```

```c
extern NSString * const WKExtendedRuntimeSessionErrorDomain;
```

## Discussion

The session passes these errors to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](./wkextendedruntimesessiondelegate/extendedruntimesession%28_,didinvalidatewith,error%29.md) method.

## See Also

### Handling Errors
- [enum WKExtendedRuntimeSessionErrorCode](./wkextendedruntimesessionerrorcode.md)
  The error codes reported by extended runtime sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrordomain)*