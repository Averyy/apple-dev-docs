# play(_:)

**Framework**: Watchkit  
**Kind**: method

Gives haptic feedback to the user.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func play(_ type: WKHapticType)
```

## Overview

Use this method to engage the haptic engine in Apple Watch. The type of feedback you specify defines the specific feedback that is delivered.

This method has no effect when called while your shared [`WKExtension`](https://developer.apple.com/documentation/watchkit/wkextension) object’s [`applicationState`](https://developer.apple.com/documentation/watchkit/wkextension/applicationstate) property is either [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) or [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive). By default, you cannot play haptic feedback in the background. The only exception are apps with an active workout session. For more information, see [`Running workout sessions`](https://developer.apple.com/documentation/HealthKit/running-workout-sessions) in [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession).

Do not call this method multiple times in quick succession. If the haptic engine is already engaged when you call this method, the system stops the current feedback and imposes a minimum delay of 100 milliseconds before engaging the engine to generate the new feedback. Use of the haptic engine also consumes power, and using the engine too much may create a noticeable drain on the Apple Watch battery, as well as a negative user experience.

> ❗ **Important**:  Do not call this method while gathering heart rate data using HealthKit. When you engage the haptic engine, HealthKit stops gathering heart rate data until after the haptic engine finishes.

 Do not call this method while gathering heart rate data using HealthKit. When you engage the haptic engine, HealthKit stops gathering heart rate data until after the haptic engine finishes.

## Parameters

- `type`: The type of haptic feedback to play. Always use the defined haptic types for their intended purposes. For a list of possible values, see  .

## See Also

- [enum WKHapticType](wkhaptictype.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/play(_:))*