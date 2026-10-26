# SetFallbackUnicodeToText

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by theUnicode converter object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus SetFallbackUnicodeToText(UnicodeToTextInfo iUnicodeToTextInfo, UnicodeToTextFallbackUPP iFallback, OptionBits iControlFlags, LogicalAddress iInfoPtr);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

You can define multiple fallback handlers and associate themwith different Unicode converter objects, depending on your requirements.See  [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md)  fora description of how to create and install an application-definedfallback handler.

You can use a fallback handler when one of the Unicode conversionfunctions,  [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) , [`ConvertFromUnicodeToTextRun`](./api-1433511-convertfromunicodetotextrun.md) , [`ConvertFromUnicodeToPString`](./api-1433581-convertfromunicodetopstring.md) ,and  [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md) ,cannot convert the text using the mapping table specified by theUnicode converter object passed to the function. 

## Parameters

- `iUnicodeToTextInfo`: The Unicode converter object to which the fallback handler is to be associated. You use the function [`CreateUnicodeToTextInfo`](./api-1433522-createunicodetotextinfo.md) or [`CreateUnicodeToTextInfoByEncoding`](./api-1433550-createunicodetotextinfobyencodin.md) to obtain a Unicode converter object of this type. 
- `iFallback`: A universal procedure pointer to the application-defined fallback routine. For a description of the function prototype that your fallback handler must adhere to and how to create your own fallback handler, see [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md). You should use the `NewUnicodeToTextFallbackProc` macro to convert a pointer to your fallback handler into a `UnicodeToTextFallbackUPP`. 
- `iControlFlags`: Control flags that stipulate which fallback handler the Unicode Converter should call—the application-defined fallback handler or the default handler—if a fallback handler is required, and the sequence in which the Unicode Converter should call the fallback handlers if either can be used when the other fails or is unavailable. See [Fallback Handler Selectors](./api-1433507-fallback_handler_selectors.md). 
- `iInfoPtr`: A point to a block of memory to be passed to the application-defined fallback handler. The Unicode Converter passes this pointer to the application-defined fallback handler as the last parameter when it calls the fallback handler. Your application can use this memory block to store data required by your fallback handler whenever it is called. This is similar in use to a reference constant (refcon). If you don’t need to use a memory block, specify `NULL` for this parameter. 

## See Also

### Setting the Fallback Handler
- [SetFallbackUnicodeToTextRun](./api-1433644-setfallbackunicodetotextrun.md)
  Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by a Unicodeconverter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433614-setfallbackunicodetotext)*