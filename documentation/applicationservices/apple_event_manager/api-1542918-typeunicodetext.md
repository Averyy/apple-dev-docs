# typeUnicodeText

**Framework**: Application Services

#### Overview

In OS X version 10.4, you should use `typeUTF16ExternalRepresentation` or `typeUTF8Text` to represent text. In earlier versions of macOS, the recommended text type is `typeUnicodeText`. All of the other constants in this enum are deprecated due to their lack of explicit encoding or byte order definition.

The implicitly encoded text types, `typeText`, `typeCString`, and `typePString`, are all deprecated in macOS, because they are incapable of representing international characters and may be reinterpreted in unpredictable ways. Additionally, `typeCString` and `typePString` do not support the full range of text coercions, and will be removed entirely in a future release. `typeStyledText` and `typeIntlText`, while they have explicit encodings, are not recommended, since they are incapable of representing Unicode-only characters, such as Hungarian, Arabic, or Thai.

## Topics

### Constants
- [var typeUTF16ExternalRepresentation: DescType](../coreservices/typeutf16externalrepresentation.md)
- [var typeUnicodeText: DescType](../coreservices/typeunicodetext.md)
  Unicode text. Native byte ordering, optional BOM.
- [var typeStyledUnicodeText: DescType](../coreservices/typestyledunicodetext.md)
  Styled Unicode text. Not implemented.
- [var typeUTF8Text: DescType](../coreservices/typeutf8text.md)
  8-bit Unicode (UTF-8 encoding).
- [var typeEncodedString: DescType](../coreservices/typeencodedstring.md)
  Styled Unicode text. Not implemented.
- [var typeCString: DescType](../coreservices/typecstring.md)
  C string—Mac OS Roman characters followed by a NULL byte. Deprecated.
- [var typePString: DescType](../coreservices/typepstring.md)
  Pascal string—unsigned length byte followed by Mac OS Roman characters. Deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/apple_event_manager/1542918-typeunicodetext)*