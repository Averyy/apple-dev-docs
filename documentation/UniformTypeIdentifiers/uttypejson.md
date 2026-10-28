# UTTypeJSON

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

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

```c
extern UTType * const UTTypeJSON;
```

## Discussion

The identifier for this type is `public.json`.

This type conforms to [`UTTypeText`](./uttypetext.md); it doesn’t conform to [`UTTypeJavaScript`](./uttypejavascript.md).

## See Also

### Data interchange formats
- [UTTypeDelimitedText](./uttypedelimitedtext.md)
  A base type that represents text containing delimited values.
- [UTTypeCommaSeparatedText](./uttypecommaseparatedtext.md)
  A type that represents text containing comma-separated values.
- [UTTypeTabSeparatedText](./uttypetabseparatedtext.md)
  A type that represents text containing tab-separated values.
- [UTTypeUTF8TabSeparatedText](./uttypeutf8tabseparatedtext.md)
  A type that represents UTF-8–encoded text containing tab-separated values.
- [UTTypeRTF](./uttypertf.md)
  A type that represents Rich Text Format data.
- [UTTypeXML](./uttypexml.md)
  A type that represents generic XML data.
- [UTTypeYAML](./uttypeyaml.md)
  A type that represents Yet Another Markup Language data.
- [UTTypeVCard](./uttypevcard.md)
  A type that represents a vCard file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypejson)*