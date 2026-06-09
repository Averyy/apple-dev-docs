# resetSecureBoot()

**Framework**: Virtualization  
**Kind**: method

Clears any previously applied Secure Boot configuration and disables Secure Boot.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func resetSecureBoot() throws
```

#### Discussion

This operation clears any previously applied Secure Boot configuration, sets the “SetupMode” global variable to `1`, and disables Secure Boot in the variable store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/resetsecureboot())*