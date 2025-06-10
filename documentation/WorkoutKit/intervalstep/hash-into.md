# hash(into:)

**Framework**: WorkoutKit  
**Kind**: method

Hashes the essential components of the interval step by feeding them into the given hash function.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## See Also

- [var hashValue: Int](intervalstep/hashvalue.md)
  The hashed value of the interval step.
- [static func != (Self, Self) -> Bool](intervalstep/!=(_:_:).md)
  Returns a Boolean value that indicates whether two interval steps aren’t equal.
- [static func == (IntervalStep, IntervalStep) -> Bool](intervalstep/==(_:_:).md)
  Returns a Boolean value that indicates whether two interval steps are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/intervalstep/hash(into:))*