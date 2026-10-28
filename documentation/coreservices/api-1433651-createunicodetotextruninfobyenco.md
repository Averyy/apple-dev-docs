# CreateUnicodeToTextRunInfoByEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Based on the given text encoding specifications for theconverted text runs, creates and returns a Unicode converter objectcontaining information required for converting strings from Unicodeto one or more specified non-Unicode encodings.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus CreateUnicodeToTextRunInfoByEncoding(ItemCount iNumberOfEncodings, const TextEncoding iEncodings[], UnicodeToTextRunInfo *oUnicodeToTextInfo);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You pass a Unicode converter object returned from `CreateUnicodeToTextRunInfoByEncoding` tothe function  [`ConvertFromUnicodeToTextRun`](./api-1433511-convertfromunicodetotextrun.md) or  [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md) to identify the information to be used for the conversion. Thesetwo functions modify the contents of the Unicode converter object. 

If an error is returned, the converter object is invalid. 

## Parameters

- `iNumberOfEncodings`: The number of desired encodings. If you pass 0 for this parameter, the converter will use all of the scripts installed in the system. The primary script is the one with highest priority; `ScriptOrder`('`itlm'` resource) determines the priority of the rest. If you set the high-order bit for this parameter, the Unicode converter assumes that the `iEncodings` parameter contains a single element specifying the preferred encoding. This feature is supported for versions 1.2 or later of the converter. 
- `iEncodings`: An array of text encoding specifications for the desired encodings. Your application provides this structure to identify the encodings to be used for the conversion. The order in which you specify the encodings determines the priority of the destination encodings. If you pass `NULL` for this parameter, the converter will use all of the scripts installed in the system. The primary script is the one with highest priority and `ScriptOrder`(`'itlm`'resource) determines the priority of the rest.This feature is supported for versions 1.2 or later of the converter. 
- `oUnicodeToTextInfo`:  A pointer to a Unicode converter object for converting Unicode text strings to strings in one or more non-Unicode encodings. On return, a pointer to a Unicode converter object that holds the encodings you supply as the `iEncodings` parameter and the state information related to the conversion. 

## See Also

### Converting From Unicode to Multiple Encodings
- [ConvertFromUnicodeToTextRun](./api-1433511-convertfromunicodetotextrun.md)
  Converts a string from Unicode to one or more encodings. 
- [ConvertFromUnicodeToScriptCodeRun](./api-1433662-convertfromunicodetoscriptcoderu.md)
  Converts a string from Unicode to one or more scripts. 
- [CreateUnicodeToTextRunInfo](./api-1433632-createunicodetotextruninfo.md)
  Creates and returns a Unicode converter object containingthe information required for converting a Unicode text string tostrings in one or more non-Unicode encodings. 
- [CreateUnicodeToTextRunInfoByScriptCode](./api-1433657-createunicodetotextruninfobyscri.md)
  Based on the given script codes for the converted textruns, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to oneor more specified non-Unicode encodings.
- [DisposeUnicodeToTextRunInfo](./api-1433595-disposeunicodetotextruninfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextRunInfo](./api-1433495-resetunicodetotextruninfo.md)
  Reinitializes all state information kept by the contextobjects in TextRun conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433651-createunicodetotextruninfobyenco)*