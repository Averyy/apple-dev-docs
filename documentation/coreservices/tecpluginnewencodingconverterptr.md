# TECPluginNewEncodingConverterPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a function that determinesa conversion path for a source and destination encoding, then createsa text encoding converter object and returns a pointer to it.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OSStatus (*TECPluginNewEncodingConverterPtr)(TECObjectRef *newEncodingConverter, TECConverterContextRec *plugContext, TextEncoding inputEncoding, TextEncoding outputEncoding);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Parameters

- `newEncodingConverter`: A pointer to a converter object. On return, this points to a newly created text converter object. 
- `plugContext`: A pointer to a TEC converter context record.
- `inputEncoding`: The text encoding specification for the source text. 
- `outputEncoding`: The text encoding specification for the destination text. 

## See Also

### Callbacks
- [UnicodeToTextFallbackProcPtr](./unicodetotextfallbackprocptr.md)
  Defines a pointer to a function that convertsa Unicode text element for which there is no destination encodingequivalent in the appropriate mapping table to the fallback character sequencedefined by your fallback handler, and returns the converted charactersequence to the Unicode Converter.
- [TECPluginGetPluginDispatchTablePtr](./tecplugingetplugindispatchtableptr.md)
  Defines a pointer to a function that returnsa pointer to a plug-in dispatch table.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/tecpluginnewencodingconverterptr)*