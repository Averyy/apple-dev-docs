# UTTypeUTF8PlainText

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A type that represents plain text encoded as UTF-8.

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
extern UTType * const UTTypeUTF8PlainText;
```

## Discussion

The identifier for this type is `public.utf8-plain-text`.

This type conforms to [`UTTypePlainText`](./uttypeplaintext.md).

## See Also

### Text files
- [UTTypeText](./uttypetext.md)
  A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](./uttypeplaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF16PlainText](./uttypeutf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](./uttypeutf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional BOM.
- [UTTypeMarkdown](./uttypemarkdown.md)
  A type that represents Markdown data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeutf8plaintext)*