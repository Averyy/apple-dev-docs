# ChangeUnicodeToTextInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Changes the mapping information contained in the specifiedUnicode converter object used to convert Unicode text to a non-Unicodeencoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ChangeUnicodeToTextInfo(UnicodeToTextInfo ioUnicodeToTextInfo, ConstUnicodeMappingPtr iUnicodeMapping);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

The function replaces the mapping table information that currentlyexists in the specified Unicode converter object with the informationcontained in the new Unicode mapping structure you provide. 

`ChangeUnicodeToTextInfo` resetsthe Unicode converter object’s fields as necessary. However, itdoes not initialize or reset the conversion state maintained bythe Unicode converter object. 

This function is especially useful for converting a stringfrom Unicode if the Unicode string contains characters that requiremultiple destination encodings and you know the next destinationencoding. 

For example, you can change the other (destination) encodingof the Unicode mapping structure pointed to by the `iUnicodeMapping` parameterbefore you call the function  [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) to convert the next character or sequence of characters that requirea different destination encoding. 

If an error is returned, the Unicode converter object is invalid. 

## Parameters

- `ioUnicodeToTextInfo`: The Unicode converter object of type [`UnicodeToTextInfo`](./unicodetotextinfo.md) to be modified. You use the function [`CreateUnicodeToTextInfo`](./api-1433522-createunicodetotextinfo.md) or [`CreateUnicodeToTextInfoByEncoding`](./api-1433550-createunicodetotextinfobyencodin.md) to obtain a Unicode converter object of this type. 
- `iUnicodeMapping`: The structure of type [`UnicodeMapping`](./unicodemapping.md) to be used. This is the new mapping that replaces the existing mapping in the Unicode converter object. 

## See Also

### Converting From Unicode
- [ConvertFromUnicodeToText](./api-1433542-convertfromunicodetotext.md)
  Converts a Unicode text string to the destination encodingyou specify. 
- [CreateUnicodeToTextInfo](./api-1433522-createunicodetotextinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to a non-Unicodeencoding. 
- [CreateUnicodeToTextInfoByEncoding](./api-1433550-createunicodetotextinfobyencodin.md)
  Based on the given text encoding specification for theconverted text, creates and returns a Unicode converter object containinginformation required for converting strings from Unicode to thespecified non-Unicode encoding.
- [DisposeUnicodeToTextInfo](./api-1433564-disposeunicodetotextinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetUnicodeToTextInfo](./api-1433647-resetunicodetotextinfo.md)
  Reinitializes all state information kept by a Unicodeconverter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433509-changeunicodetotextinfo)*