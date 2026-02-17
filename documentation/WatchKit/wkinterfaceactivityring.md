# WKInterfaceActivityRing

**Framework**: WatchKit  
**Kind**: class

A view that displays data from a HealthKit activity summary object.

**Availability**:
- watchOS 2.2+

## Declaration

```swift
class WKInterfaceActivityRing
```

#### Overview

The [`WKInterfaceActivityRing`](wkinterfaceactivityring.md) view displays data from an [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) object, using the Move, Exercise, and Stand activity rings (see [`Figure 1`](wkinterfaceactivityring#1965772.md)).

![None](https://docs-assets.developer.apple.com/published/b37fb00fdf923f18d3ed7106e28251c3/media-1965772%402x.png)

The activity ring view always appears as a black rectangle with red, green, and blue concentric rings. The rings are centered in the view, and sized to fit the available space (see [`Figure 2`](wkinterfaceactivityring#1965773.md)).

![None](https://docs-assets.developer.apple.com/published/9dd245f95d37440302b7ea79dd716c84/media-1965773%402x.png)

The rings have two different ways to display a lack of data. One indicates that the activity summary is missing, and the other indicates that the activity summary’s values are set to zero. If the ring has a `nil`-valued `activitySummary` property, the rings appear empty (see See [`Figure 3`](wkinterfaceactivityring#1965774.md)). Use this to indicate that there is no summary data available for the specified day (for example, dates in the future).

![None](https://docs-assets.developer.apple.com/published/b57c2f57d583797c12f84b0d570b150c/media-1965774%402x.png)

If the summary has zero-valued quantities set for its value properties,  the ring displays a dot at the top of the ring (see [`Figure 4`](wkinterfaceactivityring#1965776.md)). Use this to indicate that the user has not yet burned any active calories, exercised, or earned any stand hours for the specified day.

![None](https://docs-assets.developer.apple.com/published/f24bf0aa1e7fa4576bc83703115b96dc/media-1965776%402x.png)

To display activity summary data from the HealthKit store, use an [`HKActivitySummaryQuery`](https://developer.apple.com/documentation/HealthKit/HKActivitySummaryQuery) object. You can also instantiate and display your own [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) objects, as needed.

To display data for a ring, the [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) object must have a non-`nil` quantity for both the corresponding value property and goal property (see the following table).

| Ring | Value property | Goal property |
| --- | --- | --- |
| Move | [`activeEnergyBurned`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/activeEnergyBurned) | [`activeEnergyBurnedGoal`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/activeEnergyBurnedGoal) |
| Exercise | [`appleExerciseTime`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/appleExerciseTime) | [`appleExerciseTimeGoal`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/appleExerciseTimeGoal) |
| Stand | [`appleStandHours`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/appleStandHours) | [`appleStandHoursGoal`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary/appleStandHoursGoal) |

The activity ring view colors a percentage of each ring based on these properties, as shown here:

```objc
ring percent = value property quantity / goal property quantity
```

## Topics

### Setting the Activity Summary
- [func setActivitySummary(HKActivitySummary?, animated: Bool)](wkinterfaceactivityring/setactivitysummary(_:animated:).md)
  Sets the activity summary displayed by the activity ring view.
### Initializing for SwiftUI
- [init()](wkinterfaceactivityring/init.md)
  Creates an activity ring view for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md)
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md)
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md)
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md)
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md)
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md)
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceMap](wkinterfacemap.md)
  An interface element that displays a noninteractive map for the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring)*