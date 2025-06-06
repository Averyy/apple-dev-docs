# utf16ExternalPlainText

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents plain text encoded as UTF-16 with an optional bill of materials.

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
static var utf16ExternalPlainText: UTType { get }
```

#### Discussion

If the bill of materials isn’t present, the encoding uses “external byte order (big-endian),

The identifier for this type is `public.utf16-external-plain-text`.

This type conforms to [`UTTypePlainText`](uttypeplaintext.md).

## See Also

- [static var text: UTType](uttype-swift.struct/text.md)
  A base type that represents all text-encoded data, including text with markup.
- [static var plainText: UTType](uttype-swift.struct/plaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [static var utf8PlainText: UTType](uttype-swift.struct/utf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [static var utf16PlainText: UTType](uttype-swift.struct/utf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf16externalplaintext)*