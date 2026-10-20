# Pass.Barcode

**Framework**: Wallet Passes  
**Kind**: dictionary  
**Role**: Object

An object that represents a barcode shown on a pass.

**Availability**:
- iOS 6.0+ - Deprecated in 9.0
- iPadOS 6.0+ - Deprecated in 9.0
- watchOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`Pass.Barcodes`](./barcodes-data.dictionary.md) instead.

## Declaration

```
object Pass.Barcode
```

## Properties

- `altText` (string) *(deprecated)*: The text displayed near the barcode. For example, a human-readable version of the barcode data in case the barcode doesn’t scan.

  The alternative text isn’t displayed for watchOS.
- `format` (string) *(required)* *(deprecated)*: The format of the barcode.

  The barcode format PKBarcodeFormatCode128 isn’t supported for watchOS.

  **Allowed Values**: `PKBarcodeFormatQR`, `PKBarcodeFormatPDF417`, `PKBarcodeFormatAztec`
- `message` (string) *(required)* *(deprecated)*: The message or payload to display as a barcode.
- `messageEncoding` (string) *(required)* *(deprecated)*: The IANA character set name of the text encoding to use to convert `message` from a string representation to a data representation that the system renders as a barcode, such as `“iso-8859-1”`

## See Also

### Adding barcodes
- [object Pass.Barcodes](./barcodes-data.dictionary.md)
  An array of barcode objects on a Pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/pass/barcode-data.dictionary)*