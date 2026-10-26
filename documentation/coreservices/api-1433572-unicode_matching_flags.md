# Unicode Matching Flags

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify matching criteria for Unicode mappings. 

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
- [kUnicodeMatchUnicodeBaseBit](./api-1433572-unicode_matching_flags/kunicodematchunicodebasebit.md)
  Excludes mappings that do not match the text encoding base of the `unicodeEncoding` field of the structure [`UnicodeMapping`](./unicodemapping.md). 
- [kUnicodeMatchUnicodeVariantBit](./api-1433572-unicode_matching_flags/kunicodematchunicodevariantbit.md)
  Excludes mappings that do not match the text encoding variant of the `unicodeEncoding` field of the specified Unicode mapping structure. 
- [kUnicodeMatchUnicodeFormatBit](./api-1433572-unicode_matching_flags/kunicodematchunicodeformatbit.md)
  Excludes mappings that do not match the text encoding format of the `unicodeEncoding` field of the specified Unicode mapping structure. 
- [kUnicodeMatchOtherBaseBit](./api-1433572-unicode_matching_flags/kunicodematchotherbasebit.md)
  Excludes mappings that do not match the text encoding base of the `otherEncoding` field of the structure [`UnicodeMapping`](./unicodemapping.md). 
- [kUnicodeMatchOtherVariantBit](./api-1433572-unicode_matching_flags/kunicodematchothervariantbit.md)
  Excludes mappings that do not match the text encoding variant of the `otherEncoding` field of the specified Unicode mapping structure.
- [kUnicodeMatchOtherFormatBit](./api-1433572-unicode_matching_flags/kunicodematchotherformatbit.md)
  Excludes mappings that do not match the text encoding format of the `otherEncoding` field of the specified Unicode mapping structure.

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
- [Unicode Matching Masks](./api-1433554-unicode_matching_masks.md)
  Used to set or test for Unicode matching flags.
- [Fallback Handler Selectors](./api-1433507-fallback_handler_selectors.md)
  Specify a fallback handler for the Unicode Converter to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433572-unicode_matching_flags)*