# Pass.NFC

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents the near-field communication (NFC) payload the device passes to an Apple Pay terminal.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- watchOS 2.0+

## Declaration

```swift
object Pass.NFC
```

#### Discussion

> **Note**:  Adding NFC to a Pass requires a special entitlement issued by Apple. For more information, see Near Field Communication in [`Getting Started with Apple Wallet`](https://developer.apple.comhttps://developer.apple.com/wallet/get-started/).

## Properties

- `encryptionPublicKey` (string) *(required)*: The public encryption key the Value Added Services protocol uses. Use a Base64-encoded X.509 SubjectPublicKeyInfo structure that contains an ECDH public key for group P256.
- `message` (string) *(required)*: The payload the device transmits to the Apple Pay terminal. The size needs to be no more than 64 bytes. The system truncates messages longer than 64 bytes.
- `requiresAuthentication` (boolean): A Boolean value that indicates whether the NFC pass requires authentication. The default value is `false`. A value of `true` requires the user to authenticate for each use of the NFC pass. This key is valid in iOS 13.1 and later. Set `sharingProhibited` to `true` to prevent users from sharing passes with older iOS versions and bypassing the authentication requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/nfc-data.dictionary)*