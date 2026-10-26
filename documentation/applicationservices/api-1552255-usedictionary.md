# UseDictionary

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Installs the designated dictionary into a speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr UseDictionary(SpeechChannel chan, Handle dictionary);
```

#### Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

#### Discussion

The `UseDictionary` functionattempts to install the dictionary data referenced by the `dictionary` parameterinto the speech channel referenced by the `chan` parameter.The synthesizer will use whatever elements of the dictionary resourceit considers useful to the speech conversion process. Some speechsynthesizers might ignore certain types of dictionary entries.

After the `UseDictionary` functionreturns, your application is free to release any storage allocatedfor the dictionary handle. The search order for application-provideddictionaries is last-in, first-searched.

All details of how an application-provided dictionary is representedwithin the speech synthesizer are dependent on the specific synthesizerimplementation and are private to the synthesizer.

Pronunciation dictionaries allow your application to overridethe default Speech Synthesis Manager pronunciations of individualwords, such as names with unusual spellings.

## Parameters

- `chan`: The speech channel into which a dictionary is to be installed.
- `dictionary`: A handle to the dictionary data. This is often a handle to a resource of type `'dict'`.

## See Also

### Installing a Pronunciation Dictionary
- [UseSpeechDictionary](./api-1463688-usespeechdictionary.md)
  Registers a speech dictionary with a speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552255-usedictionary)*