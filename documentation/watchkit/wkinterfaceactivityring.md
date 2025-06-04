# WKInterfaceActivityRing

**Framework**: Watchkit  
**Kind**: class

A view that displays data from a HealthKit activity summary object.

**Availability**:
- watchOS 2.2+

## Declaration

```swift
class WKInterfaceActivityRing
```

## Overview

The [`WKInterfaceActivityRing`](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring) view displays data from an [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) object, using the Move, Exercise, and Stand activity rings (see [`Figure 1`](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring#1965772)).

The activity ring view always appears as a black rectangle with red, green, and blue concentric rings. The rings are centered in the view, and sized to fit the available space (see [`Figure 2`](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring#1965773)).

The rings have two different ways to display a lack of data. One indicates that the activity summary is missing, and the other indicates that the activity summary’s values are set to zero. If the ring has a `nil`-valued `activitySummary` property, the rings appear empty (see See [`Figure 3`](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring#1965774)). Use this to indicate that there is no summary data available for the specified day (for example, dates in the future).

If the summary has zero-valued quantities set for its value properties,  the ring displays a dot at the top of the ring (see [`Figure 4`](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring#1965776)). Use this to indicate that the user has not yet burned any active calories, exercised, or earned any stand hours for the specified day.

To display activity summary data from the HealthKit store, use an [`HKActivitySummaryQuery`](https://developer.apple.com/documentation/HealthKit/HKActivitySummaryQuery) object. You can also instantiate and display your own [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) objects, as needed.

To display data for a ring, the [`HKActivitySummary`](https://developer.apple.com/documentation/HealthKit/HKActivitySummary) object must have a non-`nil` quantity for both the corresponding value property and goal property (see the following table).

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Ring', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Value property', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Goal property', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Move', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615772-activeenergyburned', 'type': 'reference', 'isActive': True}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615291-activeenergyburnedgoal', 'isActive': True, 'type': 'reference'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Exercise'}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615266-appleexercisetime', 'isActive': True, 'type': 'reference'}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615409-appleexercisetimegoal', 'isActive': True, 'type': 'reference'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Stand'}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615636-applestandhours', 'isActive': True, 'type': 'reference'}]}] | [{'type': 'paragraph', 'inlineContent': [{'identifier': 'doc://com.apple.documentation/documentation/healthkit/hkactivitysummary/1615113-applestandhoursgoal', 'type': 'reference', 'isActive': True}]}] |

The activity ring view colors a percentage of each ring based on these properties, as shown here:

```objc
ring percent = value property quantity / goal property quantity
```

## Code Examples

### Example

```objc
ring percent = value property quantity / goal property quantity
```

## Topics

### Setting the Activity Summary
- [func setActivitySummary(HKActivitySummary?, animated: Bool)](setactivitysummary(_:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring/setactivitysummary(_:animated:)))
  Sets the activity summary displayed by the activity ring view.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring/init()))
  Creates an activity ring view for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring)*