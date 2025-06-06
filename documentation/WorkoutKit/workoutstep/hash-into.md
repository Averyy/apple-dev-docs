# hash(into:)

**Framework**: Workoutkit  
**Kind**: method

Hashes the essential components of the workout step by feeding them into the given hash function.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## See Also

- [var hashValue: Int](workoutstep/hashvalue.md)
  The hashed value of the workout step.
- [static func != (Self, Self) -> Bool](workoutstep/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workout steps aren’t equal.
- [static func == (WorkoutStep, WorkoutStep) -> Bool](workoutstep/==(_:_:).md)
  Returns a Boolean value that indicates whether two workout steps are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutstep/hash(into:))*