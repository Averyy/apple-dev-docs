# TextToPhonemes

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Converts a buffer of textual data into phonemic data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr TextToPhonemes(SpeechChannel chan, const void *textBuf, unsigned long textBytes, Handle phonemeBuf, long *phonemeBytes);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

Converting textual data into phonemic data is particularlyuseful during application development, when you might wish to adjustphrases that your application generates to produce smoother speech.By first converting the target phrase into phonemes, you can see whatthe synthesizer will try to speak. Then you need correct only theparts that would not have been spoken the way you want.

The `TextToPhonemes` functionconverts the `textBytes` bytesof textual data pointed to by the `textBuf` parameterto phonemic data, which it writes into the relocatable block specifiedby the `phonemeBuf` parameter.If necessary, `TextToPhonemes` resizesthis relocatable block. The `TextToPhonemes` functionsets the `phonemeBytes` parameterto the number of bytes of phonemic data actually written.

If the textual data is contained in a relocatable block, ahandle to that block must be locked before the `TextToPhonemes` functionis called. 

The data returned by `TextToPhonemes` correspondsprecisely to the phonemes that would be spoken had the input textbeen sent to `SpeakText` instead.All current mode settings for the speech channel specified by `chan` areapplied to the converted speech. No callbacks are generated whilethe `TextToPhonemes` functionis generating its output. 

## Parameters

- `chan`: A speech channel whose associated synthesizer and voice are to be used for the conversion process.
- `textBuf`: A pointer to a buffer of text to be converted. 
- `textBytes`: The number of bytes of text to be converted. 
- `phonemeBuf`: A handle to a buffer to be used to store the phonemic data. The `TextToPhonemes` function may resize the relocatable block referenced by this handle.
- `phonemeBytes`: On return, a pointer to the number of bytes of phonemic data written to the handle. 

## See Also

### Converting Text To Phonemes
- [CopyPhonemesFromText](./api-1460918-copyphonemesfromtext.md)
  Converts the specified text string into its equivalent phonemic representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552235-texttophonemes)*