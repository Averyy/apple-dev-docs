# Pass.Barcodes

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that represents a barcode on a pass.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- watchOS 2.0+

## Declaration

```swift
object Pass.Barcodes
```

## Mentions

- [Creating a coupon pass](creating-a-coupon-pass.md)
- [Creating a generic pass](creating-a-generic-pass.md)
- [Creating a store card pass](creating-a-store-card-pass.md)
- [Creating a poster event pass using semantic tags](creating-an-event-pass-using-semantic-tags.md)

## Properties

- `altText` (string): The text to display near the barcode. For example, a human-readable version of the barcode data in case the barcode doesn’t scan. The alternative text isn’t displayed for watchOS.
- `format` (string) *(required)*: The format of the barcode. The barcode format PKBarcodeFormatCode128 isn’t supported for watchOS.
- `message` (string) *(required)*: The message or payload to display as a barcode.
- `messageEncoding` (string) *(required)*: The IANA character set name of the text encoding to use to convert `message` from a string representation to a data representation that the system renders as a barcode, such as `“iso-8859-1”`.

## See Also

- [object Pass.Barcode](pass/barcode-data.dictionary.md)
  An object that represents a barcode shown on a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/barcodes-data.dictionary)*