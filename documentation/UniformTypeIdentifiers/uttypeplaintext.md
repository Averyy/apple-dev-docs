# UTTypePlainText

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A type that represents text with no markup and an unspecified encoding.

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
extern UTType * const UTTypePlainText;
```

## Discussion

The identifier for this type is `public.plain-text`.

This type conforms to [`UTTypeText`](./uttypetext.md).

## See Also

### Text files
- [UTTypeText](./uttypetext.md)
  A base type that represents all text-encoded data, including text with markup.
- [UTTypeUTF8PlainText](./uttypeutf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](./uttypeutf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](./uttypeutf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](./uttypemarkdown.md)
  A type that represents Markdown data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeplaintext)*