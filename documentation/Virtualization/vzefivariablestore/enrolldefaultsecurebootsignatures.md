# enrollDefaultSecureBootSignatures()

**Framework**: Virtualization  
**Kind**: method

Enrolls the default signatures to Secure Boot databases.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func enrollDefaultSecureBootSignatures() throws
```

#### Discussion

This operation adds Microsoft Key Exchange Keys, UEFI CA signatures, and the latest UEFI revocation list to the Key Exchange Key (KEK) database, allowed signature database (db), and forbidden signature database (dbx) respectively. You can add these signatures before or after enrolling a Platform Key. The framework preserves the Platform Key, if present.

This allows Microsoft-signed Linux distributions to boot with Secure Boot enabled.

For more information about these signature files, see the [`Microsoft Secure Boot Objects repository`](https://developer.apple.comhttps://github.com/microsoft/secureboot_objects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/enrolldefaultsecurebootsignatures())*