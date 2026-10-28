# CreateUnicodeToTextInfoByEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus CreateUnicodeToTextInfoByEncoding(TextEncoding iEncoding, UnicodeToTextInfo *oUnicodeToTextInfo);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You can use this function instead of the  [`CreateUnicodeToTextInfo`](./api-1433522-createunicodetotextinfo.md)  function tocreate a Unicode converter. However, this method is less efficientinternally because the destination text encoding you specify mustbe resolved into a Unicode mapping. Using this function, you cannotspecify a version of Unicode, so a default version of Unicode is used;16-bit format is assumed.

You pass a Unicode converter object returned from the function `CreateUnicodeToTextInfoByEncoding` tothe function  [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) or  [`ConvertFromUnicodeToPString`](./api-1433581-convertfromunicodetopstring.md) to identify the information to be used for the conversion. Thesetwo functions modify the contents of the Unicode converter object. 

You pass a Unicode converter object returned from `CreateUnicodeToTextInfoByEncoding` to thefunction  [`TruncateForUnicodeToText`](./api-1433649-truncateforunicodetotext.md) to identify the information to be used to truncate the string. Thisfunction does not modify the contents of the Unicode converter object. 

## Parameters

- `iEncoding`: The text encoding specification for the destination, or converted, text. 
- `oUnicodeToTextInfo`: A pointer to a Unicode converter object of type [`UnicodeToTextInfo`](./unicodetotextinfo.md). 

## See Also

### Converting From Unicode
- [ChangeUnicodeToTextInfo](./api-1433509-changeunicodetotextinfo.md)
  Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 
- [ConvertFromUnicodeToText](./api-1433542-convertfromunicodetotext.md)
  Converts a Unicode text string to the destination encodingyou specify. 
- [CreateUnicodeToTextInfo](./api-1433522-createunicodetotextinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 
- [DisposeUnicodeToTextInfo](./api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextInfo](./api-1433647-resetunicodetotextinfo.md)
  Reinitializes all state information kept by a Unicodeconverter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433550-createunicodetotextinfobyencodin)*