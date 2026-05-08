# init(goal:alert:)

**Framework**: WorkoutKit  
**Kind**: init

Creates a new workout step with the provided goal and alerts.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 10.0+

## Declaration

```swift
init(goal: WorkoutGoal = .open, alert: (any WorkoutAlert)? = nil)
```

## Parameters

- `goal`: A goal that determines when the step ends.
- `alert`: Optional alerts used during the step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/workoutkit/workoutstep/init(goal:alert:))*