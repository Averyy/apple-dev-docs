# ConvertFromUnicodeToTextRun

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a string from Unicode to one or more encodings. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ConvertFromUnicodeToTextRun(UnicodeToTextRunInfo iUnicodeToTextInfo, ByteCount iUnicodeLen, const UniChar iUnicodeStr[], OptionBits iControlFlags, ItemCount iOffsetCount, const ByteOffset iOffsetArray[], ItemCount *oOffsetCount, ByteOffset oOffsetArray[], ByteCount iOutputBufLen, ByteCount *oInputRead, ByteCount *oOutputLen, LogicalAddress oOutputStr, ItemCount iEncodingRunBufLen, ItemCount *oEncodingRunOutLen, TextEncodingRun oEncodingRuns[]);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

To use the `ConvertFromUnicodeToTextRun` function,you must first set up an array of structures of type  [`UnicodeMapping`](./unicodemapping.md)  containing,in order of precedence, the mapping information for the conversion.To create a Unicode converter object, you call the `CreateUnicodeToTextRunInfo` functionpassing it the Unicode mapping array, or you can the `CreateUnicodeToTextRunInfoByEncoding` or `CreateUnicodeToTextRunInfoByScriptCode` functions,which take arrays of text encodings or script codes instead of anarray of Unicode mappings. You pass the returned Unicode converterobject as the `iUnicodeToTextInfo` parameterwhen you call the `ConvertFromUnicodeToTextRun` function.

Two of the control flags that you can set for the `iControlFlags` parameterallow you to control how the Unicode Converter uses the multipleencodings in converting the text string. These flags are explainedin the description of the `iControlFlags` parameter.Here is a summary of how to use these two control flags:

-  To keep the converted text in a single encoding,clear the text-run control flag. 
-  To keep as much contiguous converted text as possible inone encoding, set the text-run control flag and clear the keep-same-encodingcontrol flag.  
-  To minimize the number of resulting encoding runs and thechanges of destination encoding, set both the text-run and keep-same-encodingcontrol flags.  

The `ConvertFromUnicodeToTextRun` functionreturns the converted string in the array pointed to by the `oOutputStr` parameter.Beginning with the first text element in the `oOutputStr` array,the elements of the array pointed to by the `oEncodingRuns` parameter identifythe encodings of the converted string. The number of elements inthe `oEncodingRuns` arraymay not correspond to the number of elements in the `oOutputStr` array.This is because the `oEncodingRuns` arrayincludes only elements for the beginning of each new encoding runin the converted string.  

## Parameters

- `iUnicodeToTextInfo`: You use the function [`CreateUnicodeToTextRunInfo`](./api-1433632-createunicodetotextruninfo.md), [`CreateUnicodeToTextRunInfoByEncoding`](./api-1433651-createunicodetotextruninfobyenco.md), or [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md) to obtain a Unicode converter object to specify for this parameter. 
- `iUnicodeLen`: The length in bytes of the Unicode string to be converted. 
- `iUnicodeStr`: A pointer to the Unicode string to be converted. 
- `iControlFlags`: Conversion control flags. The following constants define the masks for control flags valid for this parameter. You can use [Conversion Masks](./api-1433493-conversion_masks.md) and [Directionality Masks](./api-1433620-directionality_masks.md) to set the `iControlFlags` parameter. 

  If the text-run control flag is clear, `ConvertFromUnicodeToTextRun` attempts to convert the Unicode text to the single encoding it chooses from the list of encodings in the Unicode mapping structures array that you provide when you create the Unicode converter object. This is the encoding that produces the best result, that is, that provides for the greatest amount of source text conversion. If the complete source text can be converted into more than one of the encodings specified in the Unicode mapping structures array, then the converter chooses among them based on their order in the array. If this flag is clear, the `oEncodingRuns` parameter always points to a value equal to 1. 

  If you set the use-fallbacks control flag, the converter uses the default fallback characters for the current encoding. If the converter cannot handle a character using the current encoding, even using fallbacks, the converter attempts to convert the character using the other encodings, beginning with the first encoding specified in the list and skipping the encoding where it failed. 

  If you set the `kUnicodeTextRunBit` control flag, the converter attempts to convert the complete Unicode text string into the first encoding specified in the Unicode mapping structures array you passed to `CreateUnicodeToTextRunInfo`, `CreateUnicodeToTextRunInfoByEncoding`, or `CreateUnicodeToTextRunInfoByScriptCod`e when you created the Unicode converter object for this conversion. If it cannot do this, the converter then attempts to convert the first text element that failed to the remaining encodings, in their specified order in the array. What the converter does with the next text element depends on the setting of the keep-same-encoding control flag.

  If the keep-same-encoding control flag is clear, the converter returns to the original encoding and attempts to continue conversion with that encoding; this is equivalent to converting each text element to the first encoding that works, in the order specified. 

  If the keep-same-encoding control flag is set, the converter continues with the new destination encoding until it encounters a text element that cannot be converted using the new encoding. This attempts to minimize the number of encoding changes in the output text. When the converter cannot convert a text element using any of the encodings in the list and the Unicode-keep-same-encoding control flag is set, the converter uses the fallbacks default characters for the current encoding.
- `iOffsetCount`: The number of offsets in the array pointed to by the `iOffsetArray` parameter. Your application supplies this value. If you don’t want offsets returned to you, specify `0` (zero)for this parameter. 
- `iOffsetArray`: An array of type `ByteOffset`. On input, you specify the array that contains an ordered list of significant byte offsets pertaining to the source Unicode string. These offsets may identify font or style changes, for example, in the Unicode string. If you don’t want offsets returned to your application, specify `NULL` for this parameter and `0` (zero)for `iOffsetCount`. All offsets must be less than `iUnicodeLen`. 
- `oOffsetCount`: On return, a pointer to the number of offsets that were mapped in the output stream.
- `oOffsetArray`: An array of type `ByteOffset`. On return, this array contains the corresponding new offsets for the resulting converted string.
- `iOutputBufLen`: The length in bytes of the output buffer pointed to by the `oOutputStr` parameter. Your application supplies this buffer to hold the returned converted string. The `oOutputLen` parameter may return a byte count that is less than this value if the converted byte string is smaller than the buffer size you allocated.
- `oInputRead`: On return, a pointer to the number of bytes of the Unicode source string that were converted. If the function returns a result code other than `noErr`, then this parameter returns the number of bytes that were converted before the error occurred.
- `oOutputLen`: On return, a pointer to the length in bytes of the converted string.
- `oOutputStr`: A value of type `LogicalAddress`. On input, this value points to the start of the buffer for the converted string. On output, this buffer contains the converted string in one or more encodings. When an error occurs, the `ConvertFromUnicodeToTextRun` function returns the converted string up to the character that caused the error. (For guidelines on estimating the size of the buffer needed, see the discussion following the parameter descriptions. 
- `iEncodingRunBufLen`: The number of text encoding run elements you allocated for the encoding run array pointed to by the `oEncodingRuns` parameter. The converter returns the number of valid encoding runs in the location pointed to by `oEncodingRunOutLen`. Each entry in the encoding runs array specifies the beginning offset in the converted text and its associated text encoding.
- `oEncodingRunOutLen`: On return, a pointer to a the number of valid encoding runs returned in the `oEncodingRuns` parameter.
- `oEncodingRuns`: On input, an array of structures of type `TextEncodingRun`. Your application should allocate an array with the number of elements you specify in the `iEncodingRunBufLen` parameter. On return, this array contains the encoding runs for the converted text string. Each entry in the encoding run array specifies the beginning offset in the converted text string and the associated encoding specification. 

## See Also

### Converting From Unicode to Multiple Encodings
- [ConvertFromUnicodeToScriptCodeRun](./api-1433662-convertfromunicodetoscriptcoderu.md)
  Converts a string from Unicode to one or more scripts. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433511-convertfromunicodetotextrun)*