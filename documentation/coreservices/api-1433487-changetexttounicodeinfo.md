# ChangeTextToUnicodeInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Changes the mapping information for the specified Unicodeconverter object used to convert text to Unicode to the new mappingyou provide. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ChangeTextToUnicodeInfo(TextToUnicodeInfo ioTextToUnicodeInfo, ConstUnicodeMappingPtr iUnicodeMapping);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

The function replaces the mapping table information that currentlyexists in the Unicode converter object pointed to by the `ioTextToUnicodeInfo` parameterwith the information contained in the `UnicodeMapping` structureyou supply as the `iUnicodeMapping` parameter. 

`ChangeTextToUnicodeInfo` resetsthe Unicode converter object’s fields as necessary. 

If an error is returned, the Unicode converter object is invalid. 

## Parameters

- `ioTextToUnicodeInfo`: The Unicode converter object of type [`TextToUnicodeInfo`](./texttounicodeinfo.md) containing the mapping to be modified. You use the function [`CreateTextToUnicodeInfo`](./api-1433598-createtexttounicodeinfo.md) to obtain one. 
- `iUnicodeMapping`: A structure of type [`UnicodeMapping`](./unicodemapping.md) identifying the new mapping to be used. This is the mapping that replaces the existing mapping in the Unicode converter object. 

## See Also

### Converting to Unicode
- [ConvertFromTextToUnicode](./api-1433517-convertfromtexttounicode.md)
  Converts a string from any encoding to Unicode. 
- [CreateTextToUnicodeInfo](./api-1433598-createtexttounicodeinfo.md)
  Creates and returns a Unicode converter object containinginformation required for converting strings from a non-Unicode encodingto Unicode. 
- [CreateTextToUnicodeInfoByEncoding](./api-1433560-createtexttounicodeinfobyencodin.md)
  Based on the given text encoding specification, createsand returns a Unicode converter object containing information requiredfor converting strings from the specified non-Unicode encoding toUnicode. 
- [DisposeTextToUnicodeInfo](./api-1433669-disposetexttounicodeinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetTextToUnicodeInfo](./api-1433526-resettexttounicodeinfo.md)
  Reinitializes all state information kept by the contextobjects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433487-changetexttounicodeinfo)*