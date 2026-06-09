# Pass.Barcode

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents a barcode shown on a pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 1.0+

## Declaration

```swift
object Pass.Barcode
```

## Properties

- `altText` (string): The text displayed near the barcode. For example, a human-readable version of the barcode data in case the barcode doesn’t scan. The alternative text isn’t displayed for watchOS.
- `format` (string) *(required)*: The format of the barcode. The barcode format PKBarcodeFormatCode128 isn’t supported for watchOS.
- `message` (string) *(required)*: The message or payload to display as a barcode.
- `messageEncoding` (string) *(required)*: The IANA character set name of the text encoding to use to convert `message` from a string representation to a data representation that the system renders as a barcode, such as `“iso-8859-1”`

## See Also

- [object Pass.Barcodes](pass/barcodes-data.dictionary.md)
  An array of barcode objects on a Pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/barcode-data.dictionary)*