# ConvertFromUnicodeToScriptCodeRun

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a string from Unicode to one or more scripts. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ConvertFromUnicodeToScriptCodeRun(UnicodeToTextRunInfo iUnicodeToTextInfo, ByteCount iUnicodeLen, const UniChar iUnicodeStr[], OptionBits iControlFlags, ItemCount iOffsetCount, const ByteOffset iOffsetArray[], ItemCount *oOffsetCount, ByteOffset oOffsetArray[], ByteCount iOutputBufLen, ByteCount *oInputRead, ByteCount *oOutputLen, LogicalAddress oOutputStr, ItemCount iScriptRunBufLen, ItemCount *oScriptRunOutLen, ScriptCodeRun oScriptCodeRuns[]);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

To use the `ConvertFromUnicodeToScriptCodeRun` function,you must first set up an array of script codes containing in orderof precedence the scripts to be used for the conversion. To createa Unicode converter object, you call the function  [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md).You pass the returned Unicode converter object as the `iUnicodeToTextInfo` parameterwhen you call the `ConvertFromUnicodeToScriptCodeRun` function. 

## Parameters

- `iUnicodeToTextInfo`: You use the function [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md) to obtain a Unicode converter object to specify for this parameter. 
- `iUnicodeLen`: The length in bytes of the Unicode string to be converted. 
- `iUnicodeStr`: A pointer to the Unicode string to be converted. 
- `iControlFlags`: Conversion control flags. The following constants define the masks for control flags valid for this parameter. You can use [Conversion Masks](./api-1433493-conversion_masks.md) and [Directionality Masks](./api-1433620-directionality_masks.md) to set the `iControlFlags` parameter. 

  If the text-run control flag is clear, `ConvertFromUnicodeToScriptCodeRun` attempts to convert the Unicode text to the single script from the list of scripts in the Unicode converter object that produces the best result, that is, that provides for the greatest amount of source text conversion. If the complete source text can be converted into more than one of the scripts specified in the array, then the converter chooses among them based on their order in the array. If this flag is clear, the `oScriptCodeRuns` parameter always points to a value equal to 1. 

  If you set the use-fallbacks control flag, the converter uses the default fallback characters for the current script. If the converter cannot handle a character using the current encoding, even using fallbacks, the converter attempts to convert the character using the other scripts, beginning with the first one specified in the list and skipping the one where it failed. 

  If you set the `kUnicodeTextRunBit` control flag, the converter attempts to convert the complete Unicode text string into the first script specified in the Unicode mapping structures array you passed to `CreateUnicodeToTextRunInfo`, `CreateUnicodeToTextRunInfoByEncoding`, or `CreateUnicodeToTextRunInfoByScriptCode` to create the Unicode converter object used for this conversion. If it cannot do this, the converter then attempts to convert the first text element that failed to the remaining scripts, in their specified order in the array. What the converter does with the next text element depends on the setting of the keep-same-encoding control flag: 

  If the keep-same-encoding control flag is clear, the converter returns to the original script and attempts to continue conversion with that script; this is equivalent to converting each text element to the first one that works, in the order specified. 

  If the Unicode-keep-same-encoding control flag is set, the converter continues with the new destination script until it encounters a text element that cannot be converted using the new script. This attempts to minimize the number of script code changes in the output text. When the converter cannot convert a text element using any of the scripts in the list and the Unicode-keep-same-encoding control flag is set, the converter uses the fallbacks default characters for the current script.
- `iOffsetCount`: The number of offsets in the array pointed to by the `iOffsetArray` parameter. Your application supplies this value. The number of entries in `iOffsetArray` must be fewer than half the number of bytes specified in `iUnicodeLen`. If you don’t want offsets returned to you, specify `0` (zero)for this parameter. 
- `iOffsetArray`: An array of type `ByteOffset.` On input, you specify the array that contains an ordered list of significant byte offsets pertaining to the source Unicode string. These offsets may identify font or style changes, for example, in the Unicode string. If you don’t want offsets returned to your application, specify `NULL` for this parameter and `0` (zero)for `iOffsetCount`. 
- `oOffsetCount`: On return, a pointer to the number of offsets that were mapped in the output stream.
- `oOffsetArray`: An array of type `ByteOffset`. On return, this array contains the corresponding new offsets for the resulting converted string.
- `iOutputBufLen`: The length in bytes of the output buffer pointed to by the `oOutputStr` parameter. Your application supplies this buffer to hold the returned converted string. The `oOutputLen` parameter may return a byte count that is less than this value if the converted byte string is smaller than the buffer size you allocated.
- `oInputRead`: On return, a pointer to the number of bytes of the Unicode source string that were converted. If the function returns a result code other than `noErr`, then this parameter returns the number of bytes that were converted before the error occurred.
- `oOutputLen`: On return, a pointer to the length in bytes of the converted string.
- `oOutputStr`: A buffer address. On input, this value points to the beginning of the buffer for the converted string. On return, this buffer contains the converted string in one or more encodings. When an error occurs, the `ConvertFromUnicodeToScriptCodeRun` function returns the converted string up to the character that caused the error. 
- `iScriptRunBufLen`: The number of script code run elements you allocated for the script code run array pointed to by the `oScriptCodeRuns` parameter. The converter returns the number of valid script code runs in the location pointed to by `oScriptRunOutLen`. Each entry in the script code run array specifies the beginning offset in the converted text and its associated script code.
- `oScriptRunOutLen`: A pointer to a value of type `ItemCount`. On output, this value contains the number of valid script code runs returned in the `oScriptCodeRuns` parameter.
- `oScriptCodeRuns`: An array of elements of type `ScriptCodeRun`. Your application should allocate an array with the number of elements you specify in the `iScriptRunBufLen` parameter. On return, this array contains the script code runs for the converted text string. Each entry in the array specifies the beginning offset in the converted text string and the associated script code specification. 

## See Also

### Converting From Unicode to Multiple Encodings
- [ConvertFromUnicodeToTextRun](./api-1433511-convertfromunicodetotextrun.md)
  Converts a string from Unicode to one or more encodings. 
- [CreateUnicodeToTextRunInfo](./api-1433632-createunicodetotextruninfo.md)
  Creates and returns a Unicode converter object containingthe information required for converting a Unicode text string tostrings in one or more non-Unicode encodings. 
- [CreateUnicodeToTextRunInfoByEncoding](./api-1433651-createunicodetotextruninfobyenco.md)
  Based on the given text encoding specifications for theconverted text runs, creates and returns a Unicode converter objectcontaining information required for converting strings from Unicodeto one or more specified non-Unicode encodings.
- [CreateUnicodeToTextRunInfoByScriptCode](./api-1433657-createunicodetotextruninfobyscri.md)
  Based on the given script codes for the converted textruns, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to oneor more specified non-Unicode encodings.
- [DisposeUnicodeToTextRunInfo](./api-1433595-disposeunicodetotextruninfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextRunInfo](./api-1433495-resetunicodetotextruninfo.md)
  Reinitializes all state information kept by the contextobjects in TextRun conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433662-convertfromunicodetoscriptcoderu)*