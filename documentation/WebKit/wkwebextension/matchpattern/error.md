# WKWebExtension.MatchPattern.Error

**Framework**: Webkit  
**Kind**: struct

Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct Error
```

## Topics

### Type Properties
- [static var errorDomain: String](wkwebextension/matchpattern/error/errordomain.md)
- [static var invalidHost: WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/invalidhost.md)
  Indicates that the host component was invalid.
- [static var invalidPath: WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/invalidpath.md)
  Indicates that the path component was invalid.
- [static var invalidScheme: WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/invalidscheme.md)
  Indicates that the scheme component was invalid.
- [static var unknown: WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/unknown.md)
  Indicates that an unknown error occurred.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [WKWebExtension.MatchPattern.Error.Code](wkwebextension/matchpattern/error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](wkwebextension/matchpattern.md) domain.
- [class let errorDomain: String](wkwebextension/matchpattern/errordomain.md)
  A string that identifies the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/error)*