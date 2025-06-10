# supportsActivity(_:)

**Framework**: WorkoutKit  
**Kind**: method

Returns a Boolean value that indicates whether the system supports pacer workouts for the given workout activity type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func supportsActivity(_ activity: HKWorkoutActivityType) -> Bool
```

## Parameters

- `activity`: The target workout activity type.

## See Also

- [init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType, distance: Measurement<UnitLength>, time: Measurement<UnitDuration>)](pacerworkout/init(activity:location:distance:time:).md)
  Creates a new pacer workout for the specified distance and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/pacerworkout/supportsactivity(_:))*