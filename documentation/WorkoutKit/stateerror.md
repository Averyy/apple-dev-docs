# StateError

**Framework**: Workoutkit  
**Kind**: enum

An error that occurs while previewing a workout composition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
enum StateError
```

## Topics

### Getting the error type
- [StateError.watchNotPaired](stateerror/watchnotpaired.md)
  The current device doesn’t have a paired Apple Watch.
- [StateError.workoutApplicationNotInstalled](stateerror/workoutapplicationnotinstalled.md)
  The Workout app isn’t installed on this Apple Watch.
### Getting the error description
- [var localizedDescription: String](stateerror/localizeddescription.md)
  A localized description of the error.
### Comparing state errors
- [var hashValue: Int](stateerror/hashvalue.md)
  The hashed value of the error.
- [func hash(into: inout Hasher)](stateerror/hash(into:).md)
  Hashes the essential components of the error by feeding them into the given hash function.
- [static func != (Self, Self) -> Bool](stateerror/!=(_:_:).md)
  Returns a Boolean value that indicates whether errors aren’t equal.
- [static func == (StateError, StateError) -> Bool](stateerror/==(_:_:).md)
  Returns a Boolean value that indicates whether errors are equal.
### Default Implementations
- [Equatable Implementations](stateerror/equatable-implementations.md)
- [Error Implementations](stateerror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/stateerror)*