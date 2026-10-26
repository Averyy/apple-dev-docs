# getEnrolledSecureBootSignaturesWithError:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Returns the currently enrolled Secure Boot signatures in the Key Exchange Key (KEK), allowed signature (db), and forbidden signature (dbx) databases.

**Availability**:
- macOS 27.0+

## Declaration

```objc
- (VZEFISignatureDatabaseConfiguration *) getEnrolledSecureBootSignaturesWithError:(NSError **) error;
```

#### Return Value

A `VZEFISignatureDatabaseConfiguration` object containing the enrolled signatures, or `nil` if an error occurred.

## Parameters

- `error`: If not `nil`, assigned with the error if the operation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefivariablestore/getenrolledsecurebootsignatureswitherror:)*