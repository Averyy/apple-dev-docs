# markdown

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

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

```swift
static var markdown: UTType { get }
```

#### Discussion

The identifier for this type is `net.daringfireball.markdown`.

This type conforms to [`utf8PlainText`](./utf8plaintext.md).

## See Also

### Text files
- [static var text: UTType](./text.md)
  A base type that represents all text-encoded data, including text with markup.
- [static var plainText: UTType](./plaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [static var utf8PlainText: UTType](./utf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [static var utf16PlainText: UTType](./utf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [static var utf16ExternalPlainText: UTType](./utf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional bill of materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/markdown)*