# UTTypeText

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A base type that represents all text-encoded data, including text with markup.

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
extern UTType * const UTTypeText;
```

#### Discussion

The identifier for this type is `public.text`.

This type conforms to [`UTTypeData`](./uttypedata.md) and [`UTTypeContent`](./uttypecontent.md).

## See Also

### Text files
- [UTTypePlainText](./uttypeplaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](./uttypeutf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](./uttypeutf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](./uttypeutf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](./uttypemarkdown.md)
  A type that represents Markdown data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypetext)*