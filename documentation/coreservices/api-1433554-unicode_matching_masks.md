# Unicode Matching Masks

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Used to set or test for Unicode matching flags.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUnicodeMatchUnicodeBaseMask](./api-1433554-unicode_matching_masks/kunicodematchunicodebasemask.md)
  If set, excludes mappings that do not match the text encoding base of the `unicodeEncoding` field of the structure [`UnicodeMapping`](./unicodemapping.md). If not set, the function ignores the text encoding base of that field. 
- [kUnicodeMatchUnicodeVariantMask](./api-1433554-unicode_matching_masks/kunicodematchunicodevariantmask.md)
  If set, excludes mappings that do not match the text encoding variant of the `unicodeEncoding` field of the specified Unicode mapping structure. If not set, the function ignores the text encoding variant of that field.
- [kUnicodeMatchUnicodeFormatMask](./api-1433554-unicode_matching_masks/kunicodematchunicodeformatmask.md)
  If set, excludes mappings that do not match the text encoding format of the `unicodeEncoding` field of the specified Unicode mapping structure. If not set, the function ignores the text encoding format of that field.
- [kUnicodeMatchOtherBaseMask](./api-1433554-unicode_matching_masks/kunicodematchotherbasemask.md)
  If set, excludes mappings that do not match the text encoding base of the `otherEncoding` field of the structure [`UnicodeMapping`](./unicodemapping.md). If not set, the function ignores the text encoding base of that field. 
- [kUnicodeMatchOtherVariantMask](./api-1433554-unicode_matching_masks/kunicodematchothervariantmask.md)
  If set, excludes mappings that do not match the text encoding variant of the `otherEncoding` field of the specified Unicode mapping structure. If not set, the function ignores the text encoding variant of that field.
- [kUnicodeMatchOtherFormatMask](./api-1433554-unicode_matching_masks/kunicodematchotherformatmask.md)
  If set, excludes mappings that do not match the text encoding format of the `otherEncoding` field of the specified Unicode mapping structure. If not set, the function ignores the text encoding format of that field.

## See Also

### Feature Selectors
- [Conversion Flags](./api-1433583-conversion_flags.md)
  Specify how to perform conversion of text from one encoding to another.
- [Conversion Masks](./api-1433493-conversion_masks.md)
  Set or text for conversion flags.
- [Directionality Flags](./api-1433491-directionality_flags.md)
  Specify a text direction.
- [Directionality Masks](./api-1433620-directionality_masks.md)
  Set or text for directionality bits.
- [Unicode Converter Flags](./api-1400304-unicode_converter_flags.md)
  Specify features for bug fixes in the Unicode Converter.
- [Unicode Converter Masks](./api-1400367-unicode_converter_masks.md)
  Set or test for Unicode converter flags.
- [Unicode Fallback Sequencing Flag](./api-1433597-unicode_fallback_sequencing_flag.md)
  Specifies options for setting fallback sequencing.
- [Unicode Fallback Sequencing Masks](./api-1433622-unicode_fallback_sequencing_mask.md)
  Set or text for Unicode sequencing flag.
- [Unicode Matching Flags](./api-1433572-unicode_matching_flags.md)
  Specify matching criteria for Unicode mappings. 
- [Fallback Handler Selectors](./api-1433507-fallback_handler_selectors.md)
  Specify a fallback handler for the Unicode Converter to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433554-unicode_matching_masks)*