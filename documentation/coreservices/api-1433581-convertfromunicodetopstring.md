# ConvertFromUnicodeToPString

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a Unicode string to Pascal in a Mac OS text encoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus ConvertFromUnicodeToPString(UnicodeToTextInfo iUnicodeToTextInfo, ByteCount iUnicodeLen, const UniChar iUnicodeStr[], Str255 oPascalStr);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

The `ConvertFromUnicodeToPString ` functionprovides an easy and efficient way to convert a Unicode string toa Pascal string in a Mac OS text encoding without incurring the overheadassociated with use of the function  [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md)  or  [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md). 

If necessary, this function uses the loose mapping and fallbackcharacters to map the text elements of the string. For fallbackmappings, it uses the handler associated with the Unicode converterobject.  

## Parameters

- `iUnicodeToTextInfo`: A Unicode converter object. You use the `CreateUnicodeToTextInfo` or `CreateUnicodeToTextInfoByEncoding` function to obtain the Unicode converter object for the conversion. 
- `iUnicodeLen`: The length in bytes of the Unicode string to be converted. This is the string your application provides in the `iUnicodeStr` parameter. 
- `iUnicodeStr`: A pointer to an array containing the Unicode string to be converted. 
- `oPascalStr`: A buffer. On return, the converted Pascal string returned by the function. 

## See Also

### Converting Between Unicode and Pascal Strings
- [ConvertFromPStringToUnicode](./api-1433483-convertfrompstringtounicode.md)
  Converts a Pascal string in a Mac OS text encoding toa Unicode string. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433581-convertfromunicodetopstring)*