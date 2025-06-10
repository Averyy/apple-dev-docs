# handoffUserActivityType

**Framework**: UIKit  
**Kind**: property

The type of the pending Handoff activity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var handoffUserActivityType: String? { get }
```

#### Discussion

When a Handoff activity is pending at scene-connection time, UIKit puts the type of that activity in this property. Use this information at connection time to prepare your scene to receive the actual activity object. After your scene connects, UIKit calls the appropriate delegate methods to deliver the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object.

If the value of this property is `nil`, no Handoff activity is pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/handoffuseractivitytype)*