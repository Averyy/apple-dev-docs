# enableSecureBoot(platformKey:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Enables Secure Boot with a custom Platform Key.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func enableSecureBoot(platformKey: SecCertificate) throws
```

```objc
- (BOOL) enableSecureBootWithPlatformKey:(SecCertificateRef) platformKey error:(NSError **) error;
```

## Parameters

- `platformKey`: A custom Platform Key as an X.509 certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/enablesecureboot(platformkey:))*