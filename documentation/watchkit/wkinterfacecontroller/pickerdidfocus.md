# pickerDidFocus(_:)

**Framework**: Watchkit  
**Kind**: method

Called to let you know that the specified picker is now receiving input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func pickerDidFocus(_ picker: WKInterfacePicker)
```

## Overview

A picker becomes focused when the user taps it or when you call the [`focus()`](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/focus()) method of the picker itself. When a picker is focused, input from the Digital Crown updates the selected item.

The default implementation of this method does nothing. Subclasses can override it and use it to perform actions related to the picker receiving focus. You do not need to call `super` in your implementation.

## See Also

- [func pickerDidResignFocus(WKInterfacePicker)](pickerdidresignfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidresignfocus(_:)))
- [func pickerDidSettle(WKInterfacePicker)](pickerdidsettle(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidsettle(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidfocus(_:))*