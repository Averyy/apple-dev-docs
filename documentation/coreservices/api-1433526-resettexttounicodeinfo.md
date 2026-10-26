# ResetTextToUnicodeInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Reinitializes all state information kept by the contextobjects.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ResetTextToUnicodeInfo(TextToUnicodeInfo ioTextToUnicodeInfo);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `ioTextToUnicodeInfo`: 

## See Also

### Converting to Unicode
- [ChangeTextToUnicodeInfo](./api-1433487-changetexttounicodeinfo.md)
  Changes the mapping information for the specified Unicodeconverter object used to convert text to Unicode to the new mappingyou provide. 
- [ConvertFromTextToUnicode](./api-1433517-convertfromtexttounicode.md)
  Converts a string from any encoding to Unicode. 
- [CreateTextToUnicodeInfo](./api-1433598-createtexttounicodeinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from a non-Unicode encodingto Unicode. 
- [CreateTextToUnicodeInfoByEncoding](./api-1433560-createtexttounicodeinfobyencodin.md)
  Based on the given text encoding specification, createsand returns a Unicode converter object containing information requiredfor converting strings from the specified non-Unicode encoding toUnicode. 
- [DisposeTextToUnicodeInfo](./api-1433669-disposetexttounicodeinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433526-resettexttounicodeinfo)*