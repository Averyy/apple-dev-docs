# ConvertFromUnicodeToText

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a Unicode text string to the destination encodingyou specify. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ConvertFromUnicodeToText(UnicodeToTextInfo iUnicodeToTextInfo, ByteCount iUnicodeLen, const UniChar iUnicodeStr[], OptionBits iControlFlags, ItemCount iOffsetCount, const ByteOffset iOffsetArray[], ItemCount *oOffsetCount, ByteOffset oOffsetArray[], ByteCount iOutputBufLen, ByteCount *oInputRead, ByteCount *oOutputLen, LogicalAddress oOutputStr);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

This function can also map offsets for style or font informationfrom the source text string to the returned converted string. Theconverter reads the application-supplied offsets and returns thecorresponding new offsets in the converted string. If you do notwant font or style information offsets mapped to the resulting string,you should pass `NULL` for `iOffsetArray` and `0 ` (zero) for `iOffsetCount`. 

Your application must allocate a buffer to hold the resultingconverted string and pass a pointer to the buffer in the `oOutputStr` parameter.To determine the size of the output buffer to allocate, you shouldconsider the size and content of the Unicode source string in relationto the type of encoding to which it will be converted. For example,for many encodings, such as MacRoman and Shift-JIS, the size ofthe returned string will be between half the size and the same sizeas the source Unicode string. However, for some encodings that arenot Mac OS ones, such as EUC-JP, which has some 3-byte charactersfor Kanji, the returned string could be larger than the source Unicodestring. For MacArabic and MacHebrew, the result will usually beless than half the size of the Unicode string.  

## Parameters

- `iUnicodeToTextInfo`: A Unicode converter object of type `UnicodeToTextInfo` for converting text from Unicode. You use the function [`CreateUnicodeToTextInfo`](./api-1433522-createunicodetotextinfo.md) or [`CreateUnicodeToTextInfoByEncoding`](./api-1433550-createunicodetotextinfobyencodin.md) to obtain a Unicode converter object to specify for this parameter. This function modifies the contents of the `iUnicodeToTextInfo` parameter. 
- `iUnicodeLen`: The length in bytes of the Unicode string to be converted. 
- `iUnicodeStr`: A pointer to the Unicode string to be converted. If the input text is UTF-8, which is supported for versions 1.2.1 or later of the converter, you must cast the UTF-8 buffer pointer to `ConstUniCharArrayPtr` before you can pass it as this parameter. 
- `iControlFlags`: Conversion control flags. You can use [Conversion Masks](./api-1433493-conversion_masks.md) and [Directionality Masks](./api-1433620-directionality_masks.md) to set the `iControlFlags` parameter. 
- `iOffsetCount`: The number of offsets contained in the array provided by the `iOffsetArray` parameter. Your application supplies this value. If you don’t want offsets returned to you, specify `0` (zero)for this parameter. 
- `iOffsetArray`: An array of type `ByteOffset`. On input, you specify the array that gives an ordered list of significant byte offsets pertaining to the Unicode source string to be converted. These offsets may identify font or style changes, for example, in the source string. If you don’t want offsets returned to your application, specify `NULL` for this parameter and `0` (zero)for `iOffsetCount`. All offsets must be less than `iUnicodeLen`. 
- `oOffsetCount`: On return, a pointer to the number of offsets that were mapped in the output stream.
- `oOffsetArray`: An array of type `ByteOffset`. On return, this array contains the corresponding new offsets for the converted string in the new encoding.
- `iOutputBufLen`: The length in bytes of the output buffer pointed to by the `oOutputStr` parameter. Your application supplies this buffer to hold the returned converted string. The `oOutputLen` parameter may return a byte count that is less than this value if the converted byte string is smaller than the buffer size you allocated.
- `oInputRead`: On return, a pointer to a the number of bytes of the Unicode string that were converted. If the function returns a `kTECUnmappableElementErr` result code, this parameter returns the number of bytes that were converted before the error occurred.
- `oOutputLen`: On return, a pointer to the length in bytes of the converted text stream.
- `oOutputStr`: A value of type `LogicalAddress`. On input, this value points to a buffer for the converted string. On return, the buffer holds the converted text string. (For guidelines on estimating the size of the buffer needed, see the following discussion. 

## See Also

### Converting From Unicode
- [ChangeUnicodeToTextInfo](./api-1433509-changeunicodetotextinfo.md)
  Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 
- [CreateUnicodeToTextInfo](./api-1433522-createunicodetotextinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 
- [CreateUnicodeToTextInfoByEncoding](./api-1433550-createunicodetotextinfobyencodin.md)
  Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.
- [DisposeUnicodeToTextInfo](./api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextInfo](./api-1433647-resetunicodetotextinfo.md)
  Reinitializes all state information kept by a Unicodeconverter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433542-convertfromunicodetotext)*