# hash(into:)

**Framework**: Workoutkit  
**Kind**: method

Hashes the essential components of the error by feeding them into the given hash function.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## See Also

- [var hashValue: Int](stateerror/hashvalue.md)
  The hashed value of the error.
- [static func != (Self, Self) -> Bool](stateerror/!=(_:_:).md)
  Returns a Boolean value that indicates whether errors aren’t equal.
- [static func == (StateError, StateError) -> Bool](stateerror/==(_:_:).md)
  Returns a Boolean value that indicates whether errors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/stateerror/hash(into:))*