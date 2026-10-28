# setEnabled(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Enables or disables the text field.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setEnabled(_ enabled: Bool)
```

```objc
- (void) setEnabled:(BOOL) enabled;
```

## Discussion

The `enabled` value determines whether the text field responds to user interaction. For enabled text fields, tapping the text field starts the text entry process. On watchOS, the system displays the text input controller. On nearby iOS devices associated with the same iCloud account, the system displays the Apple Remote Keyboard. A disabled text field does not respond to taps.

## Parameters

- `enabled`: A Boolean value indicating whether the text field is enabled or disabled.

## See Also

### Configuring the Control
- [func setSecureTextEntry(Bool)](./setsecuretextentry%28_%29.md)
  Determines whether the text field hides the text entered by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setenabled(_:))*