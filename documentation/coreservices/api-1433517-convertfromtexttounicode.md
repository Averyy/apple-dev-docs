# ConvertFromTextToUnicode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a string from any encoding to Unicode. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ConvertFromTextToUnicode(TextToUnicodeInfo iTextToUnicodeInfo, ByteCount iSourceLen, ConstLogicalAddress iSourceStr, OptionBits iControlFlags, ItemCount iOffsetCount, const ByteOffset iOffsetArray[], ItemCount *oOffsetCount, ByteOffset oOffsetArray[], ByteCount iOutputBufLen, ByteCount *oSourceRead, ByteCount *oUnicodeLen, UniChar oUnicodeStr[]);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). The function returnsa `noErr` result code ifit has completely converted the input string to Unicode withoutusing fallback characters.

#### Discussion

You specify the source string’s encoding in the Unicodemapping structure that you pass to the function  [`CreateTextToUnicodeInfo`](./api-1433598-createtexttounicodeinfo.md)  to obtain aUnicode converter object for the conversion. You pass the Unicodeconverter object returned by `CreateTextToUnicodeInfo` to `ConvertFromTextToUnicode` asthe `iTextToUnicodeInfo` parameter. ` `

In addition to converting a text string in any encoding toUnicode, the `ConvertFromTextToUnicode` functioncan map offsets for style or font information from the source textstring to the returned converted string. The converter reads the application-suppliedoffsets, which apply to the source string, and returns the correspondingnew offsets in the converted string. If you do not want the offsetsat which font or style information occurs mapped to the resultingstring, you should pass `NULL` for `iOffsetArray` and `0 ` (zero) for `iOffsetCount`. 

Your application must allocate a buffer to hold the resultingconverted string and pass a pointer to the buffer in the `oUnicodeStr` parameter.To determine the size of the output buffer to allocate, you shouldconsider the size of the source string, its encoding type, and itscontent in relation to the resulting Unicode string. 

For example, for 1-byte encodings, such as MacRoman, the Unicodestring will be at least double the size (more if it uses noncomposedUnicode) for MacArabic and MacHebrew, the corresponding Unicodestring could be up to six times as big. For most 2-byte encodings,for example Shift-JIS, the Unicode string will be less than doublethe size. For international robustness, your application shouldallocate a buffer three to four times larger than the source string.If the output Unicode text is actually UTF-8—which could occurbeginning with the current release of the Text Encoding ConversionManager, version 1.2.1—the UTF-8 buffer pointer must be cast to `UniCharArrayPtr` beforeit can be passed as the `oUnicodeStr` parameter.Also, the output buffer length will have a wider range of variationthan for UTF-16; for ASCII input, the output will be the same size;for Han input, the output will be twice as big, and so on.  

## Parameters

- `iTextToUnicodeInfo`: A Unicode converter object of type `TextToUnicodeInfo` containing mapping and state information used for the conversion. The contents of this Unicode converter object are modified by the function. Your application obtains a Unicode converter object using the function [`CreateTextToUnicodeInfo`](./api-1433598-createtexttounicodeinfo.md). 
- `iSourceLen`: The length in bytes of the source string to be converted. 
- `iSourceStr`: The address of the source string to be converted. 
- `iControlFlags`: Conversion control flags. You can use [Conversion Masks](./api-1433493-conversion_masks.md) to set the `iControlFlags` parameter. 
- `iOffsetCount`: The number of offsets in the `iOffsetArray` parameter. Your application supplies this value. The number of entries in `iOffsetArray` must be fewer than the number of bytes specified in `iSourceLen`. If you don’t want offsets returned to you, specify `0` (zero)for this parameter. 
- `iOffsetArray`: An array of type `ByteOffset.` On input, you specify the array that contains an ordered list of significant byte offsets pertaining to the source string. These offsets may identify font or style changes, for example, in the source string. All array entries must be less than the length in bytes specified by the `iSourceLen` parameter. If you don’t want offsets returned to your application, specify `NULL` for this parameter and `0` (zero)for `iOffsetCount`. 
- `oOffsetCount`: On return, a pointer to the number of offsets that were mapped in the output stream.
- `oOffsetArray`: An array of type `ByteOffset`. On return, this array contains the corresponding new offsets for the Unicode string produced by the converter.
- `iOutputBufLen`: The length in bytes of the output buffer pointed to by the `oUnicodeStr` parameter. Your application supplies this buffer to hold the returned converted string. The `oUnicodeLen` parameter may return a byte count that is less than this value if the converted byte string is smaller than the buffer size you allocated. The relationship between the size of the source string and the Unicode string is complex and depends on the source encoding and the contents of the string.
- `oSourceRead`: On return, a pointer to the number of bytes of the source string that were converted. If the function returns a `kTECUnmappableElementErr` result code, this parameter returns the number of bytes that were converted before the error occurred.
- `oUnicodeLen`: On return, a pointer to the length in bytes of the converted stream.
- `oUnicodeStr`: A pointer to an array used to hold a Unicode string. On input, this value points to the beginning of the array for the converted string. On return, this buffer holds the converted Unicode string. (For guidelines on estimating the size of the buffer needed, see the discussion. 

## See Also

### Converting to Unicode
- [ChangeTextToUnicodeInfo](./api-1433487-changetexttounicodeinfo.md)
  Changes the mapping information for the specified Unicodeconverter object used to convert text to Unicode to the new mappingyou provide. 
- [CreateTextToUnicodeInfo](./api-1433598-createtexttounicodeinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from a non-Unicode encodingto Unicode. 
- [CreateTextToUnicodeInfoByEncoding](./api-1433560-createtexttounicodeinfobyencodin.md)
  Based on the given text encoding specification, createsand returns a Unicode converter object containing information requiredfor converting strings from the specified non-Unicode encoding toUnicode. 
- [DisposeTextToUnicodeInfo](./api-1433669-disposetexttounicodeinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetTextToUnicodeInfo](./api-1433526-resettexttounicodeinfo.md)
  Reinitializes all state information kept by the contextobjects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433517-convertfromtexttounicode)*