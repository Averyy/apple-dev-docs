# CryptoKitError.underlyingCoreCryptoError(error:)

**Framework**: Apple CryptoKit  
**Kind**: case

The underlying corecrypto library is unable to complete the requested action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case underlyingCoreCryptoError(error: Int32)
```

## See Also

- [CryptoKitError.incorrectKeySize](cryptokiterror/incorrectkeysize.md)
  The key size is incorrect.
- [CryptoKitError.invalidParameter](cryptokiterror/invalidparameter.md)
  The parameter is invalid.
- [CryptoKitError.incorrectParameterSize](cryptokiterror/incorrectparametersize.md)
  The parameter size is incorrect.
- [CryptoKitError.authenticationFailure](cryptokiterror/authenticationfailure.md)
  The authentication tag or signature is incorrect.
- [CryptoKitError.wrapFailure](cryptokiterror/wrapfailure.md)
  The framework can’t wrap the specified key.
- [CryptoKitError.unwrapFailure](cryptokiterror/unwrapfailure.md)
  The framework can’t unwrap the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/cryptokiterror/underlyingcorecryptoerror(error:))*