# TECSniffTextEncoding

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Analyzes a text stream and returns the probable encodingsin a ranked list, based on an array of possible encodings you supply.It also returns the number of errors and features for each encoding. 

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECSniffTextEncoding(TECSnifferObjectRef encodingSniffer, ConstTextPtr inputBuffer, ByteCount inputBufferLength, TextEncoding testEncodings[], ItemCount numTextEncodings, ItemCount numErrsArray[], ItemCount maxErrs, ItemCount numFeaturesArray[], ItemCount maxFeatures);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

An error indicates a code point or sequence that is illegalin the specified encoding. A feature indicates the presence of asequence that is characteristic of that encoding.

For example, the byte sequence which is interpreted in MacOS Roman as “é” could legally be interpreted either as MacOS Roman text or as Mac OS Japanese text. Both sniffers would returnzero errors, but the Mac OS Japanese sniffer would also return twofeatures of Mac OS Japanese (representing two legal 2-byte characters.)

The arrays are returned in a ranked list with the most likelytext encodings first. The results are sorted first by number oferrors (fewest to most), then by number of features (most to fewest),and then by the original order in the list. On return, the mostlikely encoding is in `testEncodings[0]` or `testEncodings[1]`.

If an encoding is not examined, its number of errors and featuresare set to 0xFFFFFFFF, and the encoding is sorted to the end ofthe list. 

## Parameters

- `encodingSniffer`: A reference to a sniffer object. 
- `inputBuffer`: The text to be sniffed. 
- `inputBufferLength`: The length of the input buffer. 
- `testEncodings`: An array of text encoding specifications. You must fill the array with the text encodings for which you want to sniff. On output, the array elements are reordered from the most likely to the least likely text encodings. 
- `numTextEncodings`: The number of entries in the `testEncodings[]` parameter. 
- `numErrsArray`: An array that must contain at least `numTextEncodings` elements. On return, an array of the number of errors found for each possible text encoding. The array elements are in the same order as the `testEncodings[]` array elements at output.
- `maxErrs`: The maximum number of errors a sniffer can encounter. The sniffer stops looking for an encoding after this number is reached.
- `numFeaturesArray`: An array of that must contain at least `numTextEncodings` elements. On return, an array of the number of features found for each possible text encoding. The array elements are in the same order as the `testEncodings[]` array elements at output.
- `maxFeatures`: The maximum number of features a sniffer can encounter. The sniffer stops looking for a features after this number is reached.

## See Also

### Using Sniffers to Investigate Encodings
- [TECCreateSniffer](./api-1571832-teccreatesniffer.md)
  Creates a sniffer object and returns a reference to it. 
- [TECClearSnifferContextInfo](./api-1571850-tecclearsniffercontextinfo.md)
  Resets a sniffer object to its initial settings so youcan reuse it.
- [TECDisposeSniffer](./api-1571854-tecdisposesniffer.md)
  Disposes of a sniffer object.
- [TECCountAvailableSniffers](./api-1571795-teccountavailablesniffers.md)
  Counts and returns the number of sniffers available inall installed plug-ins.
- [TECGetAvailableSniffers](./api-1571841-tecgetavailablesniffers.md)
  Returns the list of sniffers available in all installedplug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571836-tecsnifftextencoding)*