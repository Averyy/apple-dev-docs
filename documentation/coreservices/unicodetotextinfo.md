# UnicodeToTextInfo

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a reference to an opaque Unicode to text converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueUnicodeToTextInfo *UnicodeToTextInfo;
```

## Discussion

Many of the Unicode Converter functions that perform conversions require a Unicode converter object containing information used for the conversion process. There are three types of Unicode converter objects used for different types of conversions. You use the `UnicodeToTextInfo` type, described here, for converting from Unicode to text.

Because your application cannot directly create or modify the contents of the private Unicode converter object, the Unicode Converter provides functions to create and dispose of it. To create a Unicode converter object for converting from Unicode to text, your application must first call either the function [`CreateUnicodeToTextInfo`](./api-1433522-createunicodetotextinfo.md) or [`CreateUnicodeToTextInfoByEncoding`](./api-1433550-createunicodetotextinfobyencodin.md). 

You can then pass this object to the function [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) or [`ConvertFromUnicodeToPString`](./api-1433581-convertfromunicodetopstring.md) to identify the information used to perform the actual conversion. After you have finished using the object, you should release the memory allocated for it by calling the function [`DisposeUnicodeToTextInfo`](./api-1433564-disposeunicodetotextinfo.md).

A Unicode converter object for this purpose is defined by the `UnicodeToTextInfo` data type.  


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/unicodetotextinfo)*