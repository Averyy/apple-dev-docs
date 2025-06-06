# WeatherError

**Framework**: Weatherkit  
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
### Operators
- [static func == (WeatherError, WeatherError) -> Bool](weathererror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](weathererror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](weathererror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](weathererror/equatable-implementations.md)
- [Error Implementations](weathererror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weathererror)*