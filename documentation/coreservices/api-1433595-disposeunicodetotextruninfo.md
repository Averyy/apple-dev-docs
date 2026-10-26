# DisposeUnicodeToTextRunInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Releases the memory allocated for the specified Unicodeconverter object. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus DisposeUnicodeToTextRunInfo(UnicodeToTextRunInfo *ioUnicodeToTextRunInfo);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). If your application specifiesan invalid Unicode converter object, such as `NULL`,the function returns `paramErr`.

## Parameters

- `ioUnicodeToTextRunInfo`: A pointer to a Unicode converter object. On input, you specify a Unicode converter object that points to the conversion information to dispose. It must be an object which your application created using the function [`CreateUnicodeToTextRunInfo`](./api-1433632-createunicodetotextruninfo.md), [`CreateUnicodeToTextRunInfoByEncoding`](./api-1433651-createunicodetotextruninfobyenco.md), or [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md). You must point to any other type of Unicode converter object. Your application should not use this function with the same structure more than once. 

## See Also

### Converting From Unicode to Multiple Encodings
- [ConvertFromUnicodeToTextRun](./api-1433511-convertfromunicodetotextrun.md)
  Converts a string from Unicode to one or more encodings. 
- [ConvertFromUnicodeToScriptCodeRun](./api-1433662-convertfromunicodetoscriptcoderu.md)
  Converts a string from Unicode to one or more scripts. 
- [CreateUnicodeToTextRunInfo](./api-1433632-createunicodetotextruninfo.md)
  Creates and returns a Unicode converter object containingthe information required for converting a Unicode text string tostrings in one or more non-Unicode encodings. 
- [CreateUnicodeToTextRunInfoByEncoding](./api-1433651-createunicodetotextruninfobyenco.md)
  Based on the given text encoding specifications for theconverted text runs, creates and returns a Unicode converter objectcontaining information required for converting strings from Unicodeto one or more specified non-Unicode encodings.
- [CreateUnicodeToTextRunInfoByScriptCode](./api-1433657-createunicodetotextruninfobyscri.md)
  Based on the given script codes for the converted textruns, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to oneor more specified non-Unicode encodings.
- [ResetUnicodeToTextRunInfo](./api-1433495-resetunicodetotextruninfo.md)
  Reinitializes all state information kept by the contextobjects in TextRun conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433595-disposeunicodetotextruninfo)*