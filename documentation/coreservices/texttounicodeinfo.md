# TextToUnicodeInfo

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines reference to an opaque Unicode converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueTextToUnicodeInfo *TextToUnicodeInfo;
```

#### Discussion

A Unicode converter object is a private object containing mapping and state information. Many of the Unicode Converter functions that perform conversions require a Unicode converter object containing information used for the conversion process. There are three types of Unicode converter objects, all serving the same purpose but used for different types of conversions. You use the `TextToUnicodeInfo` type, described here, for converting from non-Unicode text to Unicode text.

Because your application cannot directly create or modify the contents of the private Unicode converter object, the Unicode Converter provides functions to create and dispose of it. To create a Unicode converter object for converting from non-Unicode text to Unicode text, your application must first call either the function [`CreateTextToUnicodeInfo`](./api-1433598-createtexttounicodeinfo.md) or the function [`CreateTextToUnicodeInfoByEncoding`](./api-1433560-createtexttounicodeinfobyencodin.md) to provide the mapping information required for the conversion. You can then pass this object to the function [`ConvertFromTextToUnicode`](./api-1433517-convertfromtexttounicode.md) or [`ConvertFromPStringToUnicode`](./api-1433483-convertfrompstringtounicode.md) to identify the information to be used in performing the actual conversion. After you have finished using the object, you should release the memory allocated for it by calling the function [`DisposeTextToUnicodeInfo`](./api-1433669-disposetexttounicodeinfo.md). The `TextToUnicodeInfo` data type defines the Unicode converter object. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/texttounicodeinfo)*