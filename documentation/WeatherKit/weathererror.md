# WeatherError

**Framework**: WeatherKit  
**Kind**: enum

An error WeatherKit returns.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum WeatherError
```

## Topics

### Getting the error type
- [WeatherError.permissionDenied](weathererror/permissiondenied.md)
  An error indicating permission denied.
- [WeatherError.unknown](weathererror/unknown.md)
  An unknown error.
### Getting the error properties
- [var errorDescription: String?](weathererror/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](weathererror/failurereason.md)
  A localized message describing the reason for the failure.
- [var helpAnchor: String?](weathererror/helpanchor.md)
  A localized message providing text if the user requests help.
- [var recoverySuggestion: String?](weathererror/recoverysuggestion.md)
  A localized message describing how to recover from the failure.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weathererror)*