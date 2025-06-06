# CopyPhonemesFromText(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Converts the specified text string into its equivalent phonemic representation.

**Availability**:
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func CopyPhonemesFromText(_ chan: SpeechChannel, _ text: CFString, _ phonemes: UnsafeMutablePointer<CFString?>) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `CopyPhonemesFromText` function is the Core Foundation-based equivalent of the [`TextToPhonemes`](1552235-texttophonemes.md) function.

Converting textual data into phonemic data is particularly useful during application development, when you might wish to adjust phrases that your application generates to produce smoother speech. By first converting the target phrase into phonemes, you can see what the synthesizer will try to speak. Then you need correct only the parts that would not have been spoken the way you want.

The data the `CopyPhonemesFromText` function stores in the `phonemes` parameter corresponds precisely to the phonemes that would be spoken had the input text been sent to `SpeakCFString` instead. All current property settings for the speech channel specified by `chan` are applied to the converted speech. No callbacks are generated while the `CopyPhonemesFromText` function is generating its output. 

## Parameters

- `chan`: A speech channel whose associated synthesizer and properties are to be used in the conversion process.
- `text`: The text from which to extract phonemic data.
- `phonemes`: On return, a   object that contains the extracted phonemic data. The caller is responsible for releasing this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460918-copyphonemesfromtext)*