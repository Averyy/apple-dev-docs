# setOn(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the state of the switch to the on or off position, optionally animating the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setOn(_ on: Bool, animated: Bool)
```

#### Discussion

Setting the switch to either position doesn’t result in an action message being sent.

## Parameters

- `on`: [`true`](https://developer.apple.com/documentation/Swift/true) if the switch should be turned to the on position; [`false`](https://developer.apple.com/documentation/Swift/false) if it should be turned to the off position. If the switch is already in the designated position, nothing happens.
- `animated`: [`true`](https://developer.apple.com/documentation/Swift/true) to animate the “flipping” of the switch; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isOn: Bool](uiswitch/ison.md)
  A Boolean value that determines whether the switch is in the on or off position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/seton(_:animated:))*