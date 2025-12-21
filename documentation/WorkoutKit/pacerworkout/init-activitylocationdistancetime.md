# init(activity:location:distance:time:)

**Framework**: WorkoutKit  
**Kind**: init

Creates a new pacer workout for the specified distance and time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(activity: HKWorkoutActivityType, location: HKWorkoutSessionLocationType = .unknown, distance: Measurement<UnitLength>, time: Measurement<UnitDuration>)
```

## Parameters

- `activity`: The workout activity type.
- `location`: The workout location.
- `distance`: The distance goal for the workout.
- `time`: The time goal for the workout.

## See Also

- [static func supportsActivity(HKWorkoutActivityType) -> Bool](pacerworkout/supportsactivity(_:).md)
  Returns a Boolean value that indicates whether the system supports pacer workouts for the given workout activity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/pacerworkout/init(activity:location:distance:time:))*