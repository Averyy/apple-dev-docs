# WKExtendedRuntimeSessionErrorDomain

**Framework**: Watchkit  
**Kind**: var

The domain for errors reported by extended runtime sessions.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
let WKExtendedRuntimeSessionErrorDomain: String
```

#### Discussion

The session passes these errors to the session delegate’s [`extendedRuntimeSession(_:didInvalidateWith:error:)`](wkextendedruntimesessiondelegate/extendedruntimesession(_:didinvalidatewith:error:).md) method.

## See Also

- [enum WKExtendedRuntimeSessionErrorCode](wkextendedruntimesessionerrorcode.md)
  The error codes reported by extended runtime sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrordomain)*