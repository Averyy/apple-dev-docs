# Fallback Handler Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify a fallback handler for the Unicode Converter to use.

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
- [kUnicodeFallbackDefaultOnly](./api-1433507-fallback_handler_selectors/kunicodefallbackdefaultonly.md)
  Use the default fallback handler only.
- [kUnicodeFallbackCustomOnly](./api-1433507-fallback_handler_selectors/kunicodefallbackcustomonly.md)
  Use the custom fallback handler only.
- [kUnicodeFallbackDefaultFirst](./api-1433507-fallback_handler_selectors/kunicodefallbackdefaultfirst.md)
  Use the default fallback handler first, then the custom one.
- [kUnicodeFallbackCustomFirst](./api-1433507-fallback_handler_selectors/kunicodefallbackcustomfirst.md)
  Use the custom fallback handler first, then the default one.

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
- [Unicode Matching Masks](./api-1433554-unicode_matching_masks.md)
  Used to set or test for Unicode matching flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433507-fallback_handler_selectors)*