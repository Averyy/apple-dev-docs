# Unicode Converter Flags

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify features for bug fixes in the Unicode Converter.

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
- [kTECKeepInfoFixBit](./api-1400304-unicode_converter_flags/kteckeepinfofixbit.md)
  This is set if the Unicode Converter has a bug fix to stop ignoring certain control flags 
- [kTECFallbackTextLengthFixBit](./api-1400304-unicode_converter_flags/ktecfallbacktextlengthfixbit.md)
- [kTECTextRunBitClearFixBit](./api-1400304-unicode_converter_flags/ktectextrunbitclearfixbit.md)
  This is set if `ConvertFromUnicodeToTextRun` and `ConvertFromUnicodeToScriptCodeRun` function correctly if the `kUnicodeTextRunBit` is clear.
- [kTECTextToUnicodeScanFixBit](./api-1400304-unicode_converter_flags/ktectexttounicodescanfixbit.md)
- [kTECAddForceASCIIChangesBit](./api-1400304-unicode_converter_flags/ktecaddforceasciichangesbit.md)
  This is set if the new control flag bits `kUnicodeForceASCIIRangeBit` and `kUnicodeNoHalfwidthCharsBit` are supported for use with the functions `ConvertFromTextToUnicode`, `ConvertFromUnicodeToText`, and so forth.
- [kTECPreferredEncodingFixBit](./api-1400304-unicode_converter_flags/ktecpreferredencodingfixbit.md)
  This is set to indicate that if a preferred encoding is specified for `CreateUnicodeToTextRunInfo` and related functions, they handle it correctly even if it does not match the system script.
- [kTECAddTextRunHeuristicsBit](./api-1400304-unicode_converter_flags/ktecaddtextrunheuristicsbit.md)
- [kTECAddFallbackInterruptBit](./api-1400304-unicode_converter_flags/ktecaddfallbackinterruptbit.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400304-unicode_converter_flags)*