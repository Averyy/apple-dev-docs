# json

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents JavaScript Object Notation (JSON) data.

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
static var json: UTType { get }
```

#### Discussion

The identifier for this type is `public.json`.

This type conforms to [`UTTypeText`](uttypetext.md); it doesn’t conform to [`UTTypeJavaScript`](uttypejavascript.md).

## See Also

- [static var delimitedText: UTType](uttype-swift.struct/delimitedtext.md)
  A base type that represents text containing delimited values.
- [static var commaSeparatedText: UTType](uttype-swift.struct/commaseparatedtext.md)
  A type that represents text containing comma-separated values.
- [static var tabSeparatedText: UTType](uttype-swift.struct/tabseparatedtext.md)
  A type that represents text containing tab-separated values.
- [static var utf8TabSeparatedText: UTType](uttype-swift.struct/utf8tabseparatedtext.md)
  A type that represents UTF-8–encoded text containing tab-separated values.
- [static var rtf: UTType](uttype-swift.struct/rtf.md)
  A type that represents Rich Text Format data.
- [static var xml: UTType](uttype-swift.struct/xml.md)
  A type that represents generic XML data.
- [static var yaml: UTType](uttype-swift.struct/yaml.md)
  A type that represents Yet Another Markup Language data.
- [static var vCard: UTType](uttype-swift.struct/vcard.md)
  A type that represents a vCard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/json)*