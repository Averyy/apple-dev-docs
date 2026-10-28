# setOn(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the state of the switch to the specified value.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setOn(_ on: Bool)
```

```objc
- (void) setOn:(BOOL) on;
```

## Discussion

Use this method to set the value of a switch. If you want to know the value of a switch, use a local variable to track that information.

## Parameters

- `on`: A Boolean value indicating whether the switch should be set to the On or Off state. Specify [`true`](../../Swift/true.md) to set the switch to the On state.

## See Also

### Configuring the Switch
- [func setColor(UIColor?)](./setcolor%28_%29.md)
  Changes the tint color of the switch when it is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/seton(_:))*