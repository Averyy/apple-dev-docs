# forceTouchCapability

**Framework**: UIKit  
**Kind**: property

The force touch capability value of the trait collection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var forceTouchCapability: UIForceTouchCapability { get }
```

## Mentions

- [Checking the availability of 3D Touch](checking-the-availability-of-3d-touch.md)

#### Discussion

3D Touch is available only on certain devices. On those devices, availability is determined by the user’s associated accessibility setting in the Settings app. Check this property’s value on app launch, and in your implementation of the [`traitCollectionDidChange(_:)`](uitraitenvironment/traitcollectiondidchange(_:).md) method.

If this property does not contain a value, the meaning is equivalent to the value [`UIForceTouchCapability.unknown`](uiforcetouchcapability/unknown.md).

## See Also

- [enum UIForceTouchCapability](uiforcetouchcapability.md)
  Keys that indicate the availability of 3D Touch on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/forcetouchcapability)*