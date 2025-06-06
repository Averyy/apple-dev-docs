# setEnabled(_:)

**Framework**: Watchkit  
**Kind**: method

Enables or disables the picker.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setEnabled(_ enabled: Bool)
```

#### Discussion

A disabled picker does not respond to taps in its content area and cannot receive focus. When the user selects an item in an enabled picker, WatchKit executes the associated action method (if any) in your WatchKit extension code.

## Parameters

- `enabled`: A Boolean value indicating whether the picker is enabled or disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setenabled(_:))*