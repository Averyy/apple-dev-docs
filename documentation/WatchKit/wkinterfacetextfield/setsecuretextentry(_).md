# setSecureTextEntry(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the text field hides the text entered by the user.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setSecureTextEntry(_ secureTextEntry: Bool)
```

```objc
- (void) setSecureTextEntry:(BOOL) secureTextEntry;
```

#### Discussion

Pass [`true`](../../Swift/true.md) to help keep passwords and other secure data private. When you enable secure text entry, the system displays a series of dots instead of the text entered by the user.

## See Also

### Configuring the Control
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Enables or disables the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setsecuretextentry(_:))*