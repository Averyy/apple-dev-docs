# utf8TabSeparatedText

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents UTF-8–encoded text containing tab-separated values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var utf8TabSeparatedText: UTType { get }
```

## Discussion

The identifier for this type is `public.utf8-tab-separated-values-text`.

This type conforms to [`UTTypeDelimitedText`](../uttypedelimitedtext.md) and [`UTTypeUTF8PlainText`](../uttypeutf8plaintext.md).

## See Also

### Data interchange formats
- [static var delimitedText: UTType](./delimitedtext.md)
  A base type that represents text containing delimited values.
- [static var commaSeparatedText: UTType](./commaseparatedtext.md)
  A type that represents text containing comma-separated values.
- [static var tabSeparatedText: UTType](./tabseparatedtext.md)
  A type that represents text containing tab-separated values.
- [static var rtf: UTType](./rtf.md)
  A type that represents Rich Text Format data.
- [static var xml: UTType](./xml.md)
  A type that represents generic XML data.
- [static var yaml: UTType](./yaml.md)
  A type that represents Yet Another Markup Language data.
- [static var json: UTType](./json.md)
  A type that represents JavaScript Object Notation (JSON) data.
- [static var vCard: UTType](./vcard.md)
  A type that represents a vCard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf8tabseparatedtext)*