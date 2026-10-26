# UTTypeMarkdown

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A type that represents Markdown data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```c
extern UTType * const UTTypeMarkdown;
```

#### Discussion

The identifier for this type is `net.daringfireball.markdown`.

This type conforms to [`UTTypeUTF8PlainText`](./uttypeutf8plaintext.md).

## See Also

### Text files
- [UTTypeText](./uttypetext.md)
  A base type that represents all text-encoded data, including text with markup.
- [UTTypePlainText](./uttypeplaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [UTTypeUTF8PlainText](./uttypeutf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [UTTypeUTF16PlainText](./uttypeutf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [UTTypeUTF16ExternalPlainText](./uttypeutf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional BOM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypemarkdown)*