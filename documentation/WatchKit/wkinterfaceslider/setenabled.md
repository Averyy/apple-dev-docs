# setEnabled(_:)

**Framework**: WatchKit  
**Kind**: method

Enables or disables the slider.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setEnabled(_ enabled: Bool)
```

#### Discussion

A disabled slider does not respond to taps in its up and down buttons. When the user taps an enabled slider, WatchKit updates the slider value and executes the associated action method (if any) in your WatchKit extension.

## Parameters

- `enabled`: A Boolean value indicating whether the slider is enabled or disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceslider/setenabled(_:))*