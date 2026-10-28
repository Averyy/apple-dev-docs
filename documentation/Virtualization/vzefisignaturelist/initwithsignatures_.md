# initWithSignatures:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Creates a signature list from the provided signatures.

**Availability**:
- macOS 27.0+

## Declaration

```objc
- (instancetype) initWithSignatures:(NSArray<VZEFISignature *> *) signatures;
```

## Return Value

A new signature list object containing the specified signatures.

## Discussion

- Parameter: signatures An array of EFI signatures. This array can contain a mix of X.509 certificates and cryptographic hashes (SHA-256).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturelist/initwithsignatures:)*