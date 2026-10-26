# ResetUnicodeToTextInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Reinitializes all state information kept by a Unicodeconverter object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ResetUnicodeToTextInfo(UnicodeToTextInfo ioUnicodeToTextInfo);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `ioUnicodeToTextInfo`: 

## See Also

### Converting From Unicode
- [ChangeUnicodeToTextInfo](./api-1433509-changeunicodetotextinfo.md)
  Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 
- [ConvertFromUnicodeToText](./api-1433542-convertfromunicodetotext.md)
  Converts a Unicode text string to the destination encodingyou specify. 
- [CreateUnicodeToTextInfo](./api-1433522-createunicodetotextinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 
- [CreateUnicodeToTextInfoByEncoding](./api-1433550-createunicodetotextinfobyencodin.md)
  Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.
- [DisposeUnicodeToTextInfo](./api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433647-resetunicodetotextinfo)*