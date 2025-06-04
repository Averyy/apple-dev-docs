# pickerDidResignFocus(_:)

**Framework**: WatchKit  
**Kind**: method

Called to let you know that the specified picker is no longer receiving input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func pickerDidResignFocus(_ picker: WKInterfacePicker)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to perform actions related to the picker losing focus. You do not need to call `super` in your implementation.

## See Also

- [func pickerDidFocus(WKInterfacePicker)](pickerdidfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidfocus(_:)))
  Called to let you know that the specified picker is now receiving input from the Digital Crown.
- [func pickerDidSettle(WKInterfacePicker)](pickerdidsettle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidsettle(_:)))
  Called to let you know when the user settles on a value in a picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidresignfocus(_:))*