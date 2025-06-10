# WorkoutAlertMetric

**Framework**: WorkoutKit  
**Kind**: enum

A value that specifies the type of metric used to measure performance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
enum WorkoutAlertMetric
```

## Topics

### Determining the metric’s type
- [WorkoutAlertMetric.average](workoutalertmetric/average.md)
  The metric represents an average value.
- [WorkoutAlertMetric.current](workoutalertmetric/current.md)
  The metric represents the current value.
### Accessing the metric’s value
- [static var countPerMinute: UnitFrequency](workoutalertmetric/countperminute.md)
  The metric’s counts per minute.
### Comparing metrics
- [static func == (WorkoutAlertMetric, WorkoutAlertMetric) -> Bool](workoutalertmetric/==(_:_:).md)
  Returns a Boolean value that indicates whether two workout metrics are equal.
- [static func != (Self, Self) -> Bool](workoutalertmetric/!=(_:_:).md)
  Returns a Boolean value that indicates whether two workout metrics aren’t equal.
- [var hashValue: Int](workoutalertmetric/hashvalue.md)
  The hashed value of the workout metric.
- [func hash(into: inout Hasher)](workoutalertmetric/hash(into:).md)
  Hashes the essential components of the workout metric by feeding them into the given hash function.
### Default Implementations
- [Equatable Implementations](workoutalertmetric/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var metric: WorkoutAlertMetric](workoutalert/metric.md)
  The metric used to measure performance for the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutalertmetric)*