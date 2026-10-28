# enableSecureBootUsingDefaultPlatformKey()

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Enables Secure Boot with an Apple-managed Platform Key.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func enableSecureBootUsingDefaultPlatformKey() throws
```

```objc
- (BOOL) enableSecureBootUsingDefaultPlatformKeyWithError:(NSError **) error;
```

## Discussion

This operation overwrites the Platform Key (PK) global variable with an Apple-managed Platform Key, sets the “SetupMode” global variable to `0`, and enables Secure Boot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/enablesecurebootusingdefaultplatformkey())*