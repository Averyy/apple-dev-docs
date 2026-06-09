# enrollSecureBootSignatures(_:)

**Framework**: Virtualization  
**Kind**: method

Enrolls the given signatures to Secure Boot databases.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func enrollSecureBootSignatures(_ signatures: VZEFISignatureDatabaseConfiguration) throws
```

#### Discussion

> ⚠️ **Warning**: Make sure that the given Secure Boot signatures are valid before enabling Secure Boot, otherwise it may render the guest unbootable.

This operation appends the given signatures to the Key Exchange Key (KEK) database, allowed signature database (db), and forbidden signature database (dbx). The method ignores a signature that already exists in the database. You can add these signatures before or after enrolling a Platform Key. The framework preserves the Platform Key, if present.

Call this method multiple times to incrementally add signatures without replacing existing ones.

## Parameters

- `signatures`: Signatures to enroll in the KEK, db, and dbx signature databases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/enrollsecurebootsignatures(_:))*