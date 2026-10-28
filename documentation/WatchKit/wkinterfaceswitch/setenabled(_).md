# setEnabled(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Enables or disables the switch.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setEnabled(_ enabled: Bool)
```

```objc
- (void) setEnabled:(BOOL) enabled;
```

## Discussion

A disabled switch does not respond to taps in its content area. When the user taps an enabled switch, WatchKit executes the associated action method (if any) in your WatchKit extension.

## Parameters

- `enabled`: A Boolean value indicating whether the switch is enabled or disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/setenabled(_:))*