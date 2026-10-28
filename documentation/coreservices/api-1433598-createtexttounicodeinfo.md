# CreateTextToUnicodeInfo

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates and returns a Unicode converter object containinginformation required for converting strings from a non-Unicode encodingto Unicode. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus CreateTextToUnicodeInfo(ConstUnicodeMappingPtr iUnicodeMapping, TextToUnicodeInfo *oTextToUnicodeInfo);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You pass a Unicode converter object returned from the functionCreateTextToUnicodeInfo to the function  [`ConvertFromTextToUnicode`](./api-1433517-convertfromtexttounicode.md)  or  [`ConvertFromPStringToUnicode`](./api-1433483-convertfrompstringtounicode.md) to identify the information to be used for the conversion. Thesetwo functions modify the contents of the object. 

You pass a Unicode converter object returned from `CreateTextToUnicodeInfo` tothe function  [`TruncateForTextToUnicode`](./api-1433518-truncatefortexttounicode.md) to identify the information to be used to truncate the string. Thisfunction does not modify the contents of the Unicode converter object.

If an error is returned, the Unicode converter object is invalid. 

## Parameters

- `iUnicodeMapping`: A pointer to a structure of type `UnicodeMapping`. Your application provides this structure to identify the mapping to use for the conversion. You must supply a value of type `TextEncoding` in the  `unicodeEncoding` field of this structure. A `TextEncoding` is a  triple composed of an encoding base, an encoding variant, and a format. You can  obtain a [`UnicodeMapping`](./unicodemapping.md) value by calling the function `CreateTextEncoding`. 
- `oTextToUnicodeInfo`: On return, the Unicode converter object holds mapping table information you supplied as the `UnicodeMapping` parameter and state information related to the conversion. This information is required for conversion of a text stream in a non-Unicode encoding to Unicode. 

## See Also

### Converting to Unicode
- [ChangeTextToUnicodeInfo](./api-1433487-changetexttounicodeinfo.md)
  Changes the mapping information for the specified Unicodeconverter object used to convert text to Unicode to the new mappingyou provide. 
- [ConvertFromTextToUnicode](./api-1433517-convertfromtexttounicode.md)
  Converts a string from any encoding to Unicode. 
- [CreateTextToUnicodeInfoByEncoding](./api-1433560-createtexttounicodeinfobyencodin.md)
  Based on the given text encoding specification, createsand returns a Unicode converter object containing information requiredfor converting strings from the specified non-Unicode encoding toUnicode. 
- [DisposeTextToUnicodeInfo](./api-1433669-disposetexttounicodeinfo.md)
  Releases the memory allocated for the specified Unicodeconverter object. 
- [ResetTextToUnicodeInfo](./api-1433526-resettexttounicodeinfo.md)
  Reinitializes all state information kept by the contextobjects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433598-createtexttounicodeinfo)*