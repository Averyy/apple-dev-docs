# CreateUnicodeToTextInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus CreateUnicodeToTextInfo(ConstUnicodeMappingPtr iUnicodeMapping, UnicodeToTextInfo *oUnicodeToTextInfo);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

You pass the Unicode converter object returned from `CreateUnicodeToTextInfo` tothe function  [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) or  [`ConvertFromUnicodeToPString`](./api-1433581-convertfromunicodetopstring.md) to identify the information to be used for the conversion. Thesetwo functions modify the contents of the Unicode converter object. 

If an error is returned, the Unicode converter object is invalid. 

## Parameters

- `iUnicodeMapping`: A pointer to a structure of type [`UnicodeMapping`](./unicodemapping.md). Your application provides this structure to identify the mapping to be used for the conversion. The `unicodeEncoding` field of this structure can specify a Unicode format of `kUnicode16BitFormat` or `kUnicodeUTF8Format`. Note that the versions of the Unicode Converter prior to 1.2.1 do not support `kUnicodeUTF8Format`. 
- `oUnicodeToTextInfo`: On return, a pointer to a Unicode converter object that holds the mapping table information you supply as the `iUnicodeMapping` parameter and the state information related to the conversion. The information contained in the Unicode converter object is required for the conversion of a Unicode string to a non-Unicode encoding. 

## See Also

### Converting From Unicode
- [ChangeUnicodeToTextInfo](./api-1433509-changeunicodetotextinfo.md)
  Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 
- [ConvertFromUnicodeToText](./api-1433542-convertfromunicodetotext.md)
  Converts a Unicode text string to the destination encodingyou specify. 
- [CreateUnicodeToTextInfoByEncoding](./api-1433550-createunicodetotextinfobyencodin.md)
  Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.
- [DisposeUnicodeToTextInfo](./api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextInfo](./api-1433647-resetunicodetotextinfo.md)
  Reinitializes all state information kept by a Unicodeconverter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433522-createunicodetotextinfo)*