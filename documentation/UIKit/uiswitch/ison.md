# isOn

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the switch is in the on or off position.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isOn: Bool { get set }
```

```objc
@property (nonatomic, getter=isOn) BOOL on;
```

#### Discussion

This property allows you to retrieve and set (without animation) a value determining whether the [`UISwitch`](../uiswitch.md) object is on or off.

## See Also

### Setting the on/off state
- [func setOn(Bool, animated: Bool)](./seton%28_,animated%29.md)
  Sets the state of the switch to the on or off position, optionally animating the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswitch/ison)*