# pickerDidFocus(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Called to let you know that the specified picker is now receiving input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func pickerDidFocus(_ picker: WKInterfacePicker)
```

```objc
- (void) pickerDidFocus:(WKInterfacePicker *) picker;
```

#### Discussion

A picker becomes focused when the user taps it or when you call the [`focus()`](../wkinterfacepicker/focus%28%29.md) method of the picker itself. When a picker is focused, input from the Digital Crown updates the selected item.

The default implementation of this method does nothing. Subclasses can override it and use it to perform actions related to the picker receiving focus. You do not need to call `super` in your implementation.

## See Also

### Managing pickers
- [func pickerDidResignFocus(WKInterfacePicker)](./pickerdidresignfocus%28_%29.md)
  Called to let you know that the specified picker is no longer receiving input from the Digital Crown.
- [func pickerDidSettle(WKInterfacePicker)](./pickerdidsettle%28_%29.md)
  Called to let you know when the user settles on a value in a picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidfocus(_:))*