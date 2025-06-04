# pickerDidSettle(_:)

**Framework**: Watchkit  
**Kind**: method

Called to let you know when the user settles on a value in a picker.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func pickerDidSettle(_ picker: WKInterfacePicker)
```

## Overview

Use this method to perform any expensive operations associated with selecting a picker item. The user can turn the Digital Crown quickly to scroll through the items in the picker. This method is called only after scrolling subsides and the value remains steady for a reasonable period of time. For inexpensive operations, you can continue to use the picker’s action method, which is called for each change of the selected item.

The default implementation of this method does nothing. Subclasses can override it and use it to perform actions related to the picker settling on a value. You do not need to call `super` in your implementation.

## Parameters

- `picker`: The picker containing the selected value.

## See Also

- [func pickerDidFocus(WKInterfacePicker)](pickerdidfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidfocus(_:)))
- [func pickerDidResignFocus(WKInterfacePicker)](pickerdidresignfocus(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidresignfocus(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/pickerdidsettle(_:))*