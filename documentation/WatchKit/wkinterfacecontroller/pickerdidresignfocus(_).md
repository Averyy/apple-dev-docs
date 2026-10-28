# pickerDidResignFocus(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Called to let you know that the specified picker is no longer receiving input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func pickerDidResignFocus(_ picker: WKInterfacePicker)
```

```objc
- (void) pickerDidResignFocus:(WKInterfacePicker *) picker;
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to perform actions related to the picker losing focus. You do not need to call `super` in your implementation.

## See Also

### Managing pickers
- [func pickerDidFocus(WKInterfacePicker)](./pickerdidfocus%28_%29.md)
  Called to let you know that the specified picker is now receiving input from the Digital Crown.
- [func pickerDidSettle(WKInterfacePicker)](./pickerdidsettle%28_%29.md)
  Called to let you know when the user settles on a value in a picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidresignfocus(_:))*