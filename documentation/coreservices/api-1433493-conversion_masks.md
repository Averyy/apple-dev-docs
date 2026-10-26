# Conversion Masks

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Set or text for conversion flags.

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
- [kUnicodeUseFallbacksMask](./api-1433493-conversion_masks/kunicodeusefallbacksmask.md)
- [kUnicodeKeepInfoMask](./api-1433493-conversion_masks/kunicodekeepinfomask.md)
- [kUnicodeDirectionalityMask](./api-1433493-conversion_masks/kunicodedirectionalitymask.md)
  A mask for setting the directionality control flag
- [kUnicodeVerticalFormMask](./api-1433493-conversion_masks/kunicodeverticalformmask.md)
- [kUnicodeLooseMappingsMask](./api-1433493-conversion_masks/kunicodeloosemappingsmask.md)
- [kUnicodeStringUnterminatedMask](./api-1433493-conversion_masks/kunicodestringunterminatedmask.md)
- [kUnicodeTextRunMask](./api-1433493-conversion_masks/kunicodetextrunmask.md)
- [kUnicodeKeepSameEncodingMask](./api-1433493-conversion_masks/kunicodekeepsameencodingmask.md)
- [kUnicodeForceASCIIRangeMask](./api-1433493-conversion_masks/kunicodeforceasciirangemask.md)
- [kUnicodeNoHalfwidthCharsMask](./api-1433493-conversion_masks/kunicodenohalfwidthcharsmask.md)
  Sets the no halfwidth characters control flag.
- [kUnicodeTextRunHeuristicsMask](./api-1433493-conversion_masks/kunicodetextrunheuristicsmask.md)
- [kUnicodeMapLineFeedToReturnMask](./api-1433493-conversion_masks/kunicodemaplinefeedtoreturnmask.md)
- [kUnicodeUseExternalEncodingFormMask](./api-1433493-conversion_masks/kunicodeuseexternalencodingformmask.md)

## See Also

### Feature Selectors
- [Conversion Flags](./api-1433583-conversion_flags.md)
  Specify how to perform conversion of text from one encoding to another.
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
- [Fallback Handler Selectors](./api-1433507-fallback_handler_selectors.md)
  Specify a fallback handler for the Unicode Converter to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433493-conversion_masks)*