# UnicodeToTextRunInfo

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a reference to an opaque Unicode to text run information converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueUnicodeToTextRunInfo *UnicodeToTextRunInfo;
```

#### Discussion

Many of the Unicode Converter functions that perform conversions require a Unicode converter object containing information used for the conversion process. There are three types of Unicode converter objects used for different types of conversions. You use the `UnicodeToTextRunInfo` type, described here, for converting from Unicode to multiple encodings.

Because your application cannot directly create or modify the contents of the private Unicode converter object, the Unicode Converter provides functions to create and dispose of it. You can use any of three functions to create a Unicode converter object for converting from Unicode to multiple encodings. You can use [`CreateUnicodeToTextRunInfo`](./api-1433632-createunicodetotextruninfo.md), [`CreateUnicodeToTextRunInfoByEncoding`](./api-1433651-createunicodetotextruninfobyenco.md), or [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md). 

You can then pass this object to the function [`ConvertFromUnicodeToTextRun`](./api-1433511-convertfromunicodetotextrun.md) or [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md) to identify the information used to perform the actual conversion. After you have finished using the object, you should release the memory allocated for it by calling the function [`DisposeUnicodeToTextRunInfo`](./api-1433595-disposeunicodetotextruninfo.md).

A Unicode converter object for this purpose is defined by the `UnicodeToTextRunInfo` data type.  


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/unicodetotextruninfo)*