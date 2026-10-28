# SetFallbackUnicodeToTextRun

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by a Unicodeconverter object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus SetFallbackUnicodeToTextRun(UnicodeToTextRunInfo iUnicodeToTextRunInfo, UnicodeToTextFallbackUPP iFallback, OptionBits iControlFlags, LogicalAddress iInfoPtr);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You can define multiple fallback handlers and associate themwith different Unicode converter objects, depending on your requirements.See [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md) for adescription of how to create and install an application-definedfallback handler. 

## Parameters

- `iUnicodeToTextRunInfo`: The Unicode converter object to which the fallback handler is to be associated. You use the function [`CreateUnicodeToTextRunInfo`](./api-1433632-createunicodetotextruninfo.md), [`CreateUnicodeToTextRunInfoByEncoding`](./api-1433651-createunicodetotextruninfobyenco.md), or [`CreateUnicodeToTextRunInfoByScriptCode`](./api-1433657-createunicodetotextruninfobyscri.md) to obtain a Unicode converter object to specify for this parameter. 
- `iFallback`: A universal procedure pointer to the application-defined fallback routine. For a description of the function prototype to which your fallback handler must adhere and how to create your own fallback handler, see [`UnicodeToTextFallbackProcPtr`](./unicodetotextfallbackprocptr.md). You should use the `NewUnicodeToTextFallbackProc` macro described in the discussion of the function [`SetFallbackUnicodeToText`](./api-1433614-setfallbackunicodetotext.md). 
- `iControlFlags`: Control flags that stipulate which fallback handler the Unicode Converter should call—the application-defined fallback handler or the default handler—if a fallback handler is required, and the sequence in which the Unicode Converter should call the fallback handlers if either can be used when the other fails or is unavailable. See [Fallback Handler Selectors](./api-1433507-fallback_handler_selectors.md). 
- `iInfoPtr`: A pointer to a block of memory to be passed to the application-defined fallback handler. The Unicode Converter passes this pointer to the application-defined fallback handler as the last parameter when it calls the fallback handler. Your application can use this block to store data required by your fallback handler whenever it is called. This is similar in use to a reference constant(refcon). If you don’t need to use a memory block, specify `NULL` for this parameter. 

## See Also

### Setting the Fallback Handler
- [SetFallbackUnicodeToText](./api-1433614-setfallbackunicodetotext.md)
  Specifies a fallback handler to be used for convertinga Unicode text segment to another encoding when the Unicode Convertercannot convert the text using the mapping table specified by theUnicode converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1433644-setfallbackunicodetotextrun)*