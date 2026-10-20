# WKWebExtension.MatchPattern.Error

**Framework**: WebKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../matchpattern.md) domain.

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
- [static var errorDomain: String](./error/errordomain.md)
- [static var invalidHost: WKWebExtension.MatchPattern.Error.Code](./error/invalidhost.md)
  Indicates that the host component was invalid.
- [static var invalidPath: WKWebExtension.MatchPattern.Error.Code](./error/invalidpath.md)
  Indicates that the path component was invalid.
- [static var invalidScheme: WKWebExtension.MatchPattern.Error.Code](./error/invalidscheme.md)
  Indicates that the scheme component was invalid.
- [static var unknown: WKWebExtension.MatchPattern.Error.Code](./error/unknown.md)
  Indicates that an unknown error occurred.

## Relationships

### Conforms To
- [CustomNSError](../../../Foundation/customnserror.md)
- [Equatable](../../../Swift/equatable.md)
- [Error](../../../Swift/error.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Errors
- [WKWebExtension.MatchPattern.Error.Code](./error/code.md)
  Constants that indicate errors in the [`WKWebExtension.MatchPattern`](../matchpattern.md) domain.
- [class let errorDomain: String](./errordomain.md)
  A string that identifies the error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/matchpattern/error)*