# UnicodeToTextFallbackProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a function that convertsa Unicode text element for which there is no destination encodingequivalent in the appropriate mapping table to the fallback character sequencedefined by your fallback handler, and returns the converted charactersequence to the Unicode Converter.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OSStatus (*UnicodeToTextFallbackProcPtr)(UniChar *iSrcUniStr, ByteCount iSrcUniStrLen, ByteCount *oSrcConvLen, TextPtr oDestStr, ByteCount iDestStrLen, ByteCount *oDestConvLen, LogicalAddress iInfoPtr, ConstUnicodeMappingPtr iUnicodeMappingPtr);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). Your handler should return `noErr` ifit can handle the fallback, or `kTECUnmappableElementErr` ifit cannot. It can return other errors for exceptional conditions,such as when the output buffer is too small. If your handler returns `kTECUnmappableElementErr`,then `oSrcConvLen` and `oDestConvLen` areignored because either the default handler will be called or thedefault fallback sequence will be used.

#### Discussion

The Unicode Converter calls your fallback handler when itcannot convert a text string using the mapping table specified bythe Unicode converter object passed to either `ConvertFromUnicodeToText` or `ConvertFromUnicodeToPString`.The control flags you set for the `controlFlags` parameterof the function [`SetFallbackUnicodeToText`](./api-1433614-setfallbackunicodetotext.md) orthe [`SetFallbackUnicodeToTextRun`](./api-1433644-setfallbackunicodetotextrun.md) stipulatewhich fallback handler the Unicode Converter should call and whichone to try first if both can be used. 

When the Unicode Converter calls your handler, it passes toit the Unicode character to be converted and its length, a bufferfor the converted string you return and the buffer length, and apointer to a block of memory containing the data your applicationsupplied to be passed on to your fallback handler. 

After you convert the Unicode text segment to fallback characters,you return the fallback character sequence of the converted textin the buffer provided to you and the length in bytes of this fallbackcharacter sequence. You also return the length in bytes of the portion ofthe source Unicode text element that your handler actually processed. 

You provide a fallback-handler function for use with the function [`CreateUnicodeToTextInfoByEncoding`](./api-1433550-createunicodetotextinfobyencodin.md), [`ConvertFromUnicodeToPString`](./api-1433581-convertfromunicodetopstring.md), [`ConvertFromUnicodeToTextRun`](./api-1433511-convertfromunicodetotextrun.md),or [`ConvertFromUnicodeToScriptCodeRun`](./api-1433662-convertfromunicodetoscriptcoderu.md).You associate an application-defined fallback handler with a particularUnicode converter object you intend to pass to the conversion functionwhen you call it. 

Text converted from UTF-8 will already have been convertedto UTF-16 before the fallback handler is called to process it. Yourfallback handler should do all of its processing on text encodedin UTF-16. 

Your application-defined fallback handler should not movememory or call any toolbox function that would move memory. If itneeds memory, the memory should be allocated before the call to `SetFallbackUnicodeToText` or `SetFallbackUnicodeToTextRun`,and a memory reference should be passed either directly as `iInfoPtr` orin the data referenced by `iInfoPtr`.

To associate a fallback-handler function with a Unicode converterobject you use the [`SetFallbackUnicodeToText`](./api-1433614-setfallbackunicodetotext.md) and [`SetFallbackUnicodeToTextRun`](./api-1433644-setfallbackunicodetotextrun.md) functions.For these functions, you must pass a universal procedure pointer(`UniversalProcPtr`). Thisis derived from a pointer to your function by using the predefinedmacro `NewUnicodeToTextFallbackProc`. 

For versions of the Unicode Converter prior to 1.2, the fallbackhandler may receive a multiple character text element, so the sourcestring length value could be greater than 2 and the fallback handlermay set `srcConvLen` toa value greater than 2. In versions earlier than 1.2.1, the `srcConvLen` and `destConvLen` variablesare not initialized to 0; both values are ignored unless the fallbackhandler returns `noErr`. 

The following example shows how to install an application-definedfallback handler. You can name your application-defined fallbackhandler anything you choose. The name, `MyUnicodeToTextFallbackProc`,used in this example is not significant. However, you must adhereto the parameters, the return type, and the calling convention asexpressed in this example, which follows the prototype, becausea pointer to this function must be of type `UnicodeToTextFallbackProcPtr` asdefined in the `UnicodeConverter.h` headerfile. 

The `UnicodeConverter.h` headerfile also defines the `UnicodeToTextFallbackUPP` typeand the `NewUnicodeToTextFallbackProc` macro. 

## Parameters

- `iSrcUniStr`: A pointer to a single UTF-16 character to be mapped by the fallback handler. 
- `iSrcUniStrLen`: The length in bytes of the UTF-16 character indicated by the `iSrcUniStr` parameter. Usually this is 2 bytes, but it could be 4 bytes for a non-BMP character. 
- `oSrcConvLen`: On return, a pointer to the length in bytes of the portion of the Unicode character that was actually processed by your fallback handler. Your fallback handler returns this value. It should set this to 0 if none of the text was handled, or 2 or 4 if the Unicode character was handled. This value is initialized to 0 before the fallback handler is called.
- `oDestStr`: A pointer to the output buffer where your handler should place any converted text. 
- `iDestStrLen`: The maximum size in bytes of the buffer provided by the `oDestStr` parameter.
- `oDestConvLen`: On return, a pointer to the length in bytes of the fallback character sequence generated by your fallback handler. Your handler should return this length. It is initialized to 0 (zero)before the fallback handler is called.
- `iInfoPtr`: A pointer to a block of memory allocated by your application, which can be used by your fallback handler in any way that you like. This is the same pointer passed as the last parameter of `SetFallbackUnicodeToText` or `SetFallbackUnicodeToTextRun`. How you use the data passed to you in this memory block is particular to your handler. This is similar in use to a reference constant(refcon). 
- `iUnicodeMappingPtr`: A constant pointer to a structure of type [`UnicodeMapping`](./unicodemapping.md). This structure identifies a Unicode encoding specification and a particular base encoding specification. 

## See Also

### Callbacks
- [TECPluginGetPluginDispatchTablePtr](./tecplugingetplugindispatchtableptr.md)
  Defines a pointer to a function that returnsa pointer to a plug-in dispatch table.
- [TECPluginNewEncodingConverterPtr](./tecpluginnewencodingconverterptr.md)
  Defines a pointer to a function that determinesa conversion path for a source and destination encoding, then createsa text encoding converter object and returns a pointer to it.
- [TECPluginClearContextInfoPtr](./tecpluginclearcontextinfoptr.md)
  Defines a pointer to a function that resets aconverter object to its initial state.
- [TECPluginConvertTextEncodingPtr](./tecpluginconverttextencodingptr.md)
  Defines a pointer to a function that convertsstream of text from a source encoding to a destination encoding,using the conversion path specified by the converter object you supply.
- [TECPluginFlushConversionPtr](./tecpluginflushconversionptr.md)
  Defines a pointer to a function that flushesout any data in a converter object’s temporary buffers and resetsthe converter object.
- [TECPluginDisposeEncodingConverterPtr](./tecplugindisposeencodingconverterptr.md)
  Defines a pointer to a function that disposesof a converter object.
- [TECPluginNewEncodingSnifferPtr](./tecpluginnewencodingsnifferptr.md)
  Defines a pointer to a function that createsa sniffer object and returns a reference to it.
- [TECPluginClearSnifferContextInfoPtr](./tecpluginclearsniffercontextinfoptr.md)
  Defines a pointer to a function that resets asniffer object to its initial settings.
- [TECPluginSniffTextEncodingPtr](./tecpluginsnifftextencodingptr.md)
  Defines a pointer toa function that analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply;it also returns the number of errors and features for each encoding. 
- [TECPluginDisposeEncodingSnifferPtr](./tecplugindisposeencodingsnifferptr.md)
  Defines a pointer to a function that disposesof a sniffer object.
- [TECPluginGetCountAvailableTextEncodingsPtr](./tecplugingetcountavailabletextencodingsptr.md)
  Defines a pointer to a function that obtainsthe available text encodings.
- [TECPluginGetCountAvailableTextEncodingPairsPtr](./tecplugingetcountavailabletextencodingpairsptr.md)
  Defines a pointer to a function that obtainsthe available text encoding pairs.
- [TECPluginGetCountDestinationTextEncodingsPtr](./tecplugingetcountdestinationtextencodingsptr.md)
  Defines a pointer to a function that counts andreturns the number of destination encodings to which a specifiedsource encoding can be converted in one step.
- [TECPluginGetCountSubTextEncodingsPtr](./tecplugingetcountsubtextencodingsptr.md)
  Defines a pointer to a function that obtainsthe text encoding specifications for the subencodings the encodingscheme supports.
- [TECPluginGetCountAvailableSniffersPtr](./tecplugingetcountavailablesniffersptr.md)
  Defines a pointer to a function that counts andreturns the number of sniffers available in all installed plug-ins.
- [TECPluginGetCountWebEncodingsPtr](./tecplugingetcountwebencodingsptr.md)
  Defines a pointer to a function that obtainsthe available web text encodings.
- [TECPluginGetCountMailEncodingsPtr](./tecplugingetcountmailencodingsptr.md)
  Defines a pointer to a function that obtainsthe text encodings available for email.
- [TECPluginGetTextEncodingInternetNamePtr](./tecplugingettextencodinginternetnameptr.md)
  Defines a pointer to a function that obtainsthe Internet text encoding name for a text encoding specification.
- [TECPluginGetTextEncodingFromInternetNamePtr](./tecplugingettextencodingfrominternetnameptr.md)
  Defines a pointer to a function that obtainsthe text encoding for an Internet text encoding name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/unicodetotextfallbackprocptr)*