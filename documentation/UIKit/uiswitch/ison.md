# isOn

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the switch is in the on or off position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isOn: Bool { get set }
```

#### Discussion

This property allows you to retrieve and set (without animation) a value determining whether the [`UISwitch`](uiswitch.md) object is on or off.

## See Also

- [func setOn(Bool, animated: Bool)](uiswitch/seton(_:animated:).md)
  Sets the state of the switch to the on or off position, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/ison)*