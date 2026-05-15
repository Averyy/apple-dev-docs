# isValidAuthenticationCode(_:authenticating:using:)

**Framework**: Apple CryptoKit  
**Kind**: method

Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.

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
static func isValidAuthenticationCode<D>(_ authenticationCode: HMAC<H>.MAC, authenticating authenticatedData: D, using key: SymmetricKey) -> Bool where D : DataProtocol
```

#### Return Value

A Boolean value that’s `true` if the message authentication code is valid for the specified block of data.

## Parameters

- `authenticationCode`: The authentication code to compare.
- `authenticatedData`: The block of data to compare.
- `key`: The symmetric key for the authentication code.

## See Also

- [static func isValidAuthenticationCode(HMAC<H>.MAC, authenticating: UnsafeRawBufferPointer, using: SymmetricKey) -> Bool](hmac/isvalidauthenticationcode(_:authenticating:using:)-5jbc8.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.
- [static func isValidAuthenticationCode<C, D>(C, authenticating: D, using: SymmetricKey) -> Bool](hmac/isvalidauthenticationcode(_:authenticating:using:)-5ilt9.md)
  Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac/isvalidauthenticationcode(_:authenticating:using:)-8ezmw)*