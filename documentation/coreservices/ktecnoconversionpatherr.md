# kTECNoConversionPathErr

**Framework**: Core Services  
**Kind**: data

The converter supports both the source andtarget encodings, but cannot convert between them either directlyor indirectly. Returned by the Text Encoding Converter functionsonly. 

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kTECNoConversionPathErr: Int { get }
```

## See Also

- [var kTextUnsupportedEncodingErr: Int](ktextunsupportedencodingerr.md)
  The encoding or mapping is not supportedfor this function by the current set of tables or plug-ins.
- [var kTextMalformedInputErr: Int](ktextmalformedinputerr.md)
  The text input contains a sequence thatis not legal in the specified encoding, such as a DBCS high byte followedby an invalid low byte (0x8120 in Shift-JIS). 
- [var kTextUndefinedElementErr: Int](ktextundefinedelementerr.md)
  The text input contains a code point thatis undefined in the specified encoding. The function did not completelyconvert the input string. You can resume conversion from a pointbeyond the offending character, or take some other action.
- [var kTECMissingTableErr: Int](ktecmissingtableerr.md)
  The specified encoding is partially supported,but a specific table required for this function is missing.
- [var kTECTableChecksumErr: Int](ktectablechecksumerr.md)
  A specific table required for this functionhas a checksum error, indicating that it has become corrupted.
- [var kTECTableFormatErr: Int](ktectableformaterr.md)
  The table format is either invalid or itcannot be handled by the current version of the code. The function didnot convert the string
- [var kTECCorruptConverterErr: Int](kteccorruptconvertererr.md)
  The converter object is invalid. Returnedby the Text Encoding Converter functions only. 
- [var kTECBufferBelowMinimumSizeErr: Int](ktecbufferbelowminimumsizeerr.md)
  The output text buffer is too small to accommodatethe result of processing of the first input text element. No partof the input string was processed.
- [var kTECArrayFullErr: Int](ktecarrayfullerr.md)
- [var kTECPartialCharErr: Int](ktecpartialcharerr.md)
  The input text ends in the middle of a multibytecharacter and conversion stopped. Append the unconverted input fromthis call to the beginning of the subsequent input text and callthe function again.
- [var kTECUnmappableElementErr: Int](ktecunmappableelementerr.md)
  An input text element cannot be mapped tothe specified output encoding(s) using the specified options. Forthe Unicode Converter, this error can occur only if kUnicodeUseFallbacksBitcontrol flag is not set. 
- [var kTECIncompleteElementErr: Int](ktecincompleteelementerr.md)
  The input text ends with a text elementthat might be incomplete, or contains a text element that is too longfor the internal buffers. 
- [var kTECDirectionErr: Int](ktecdirectionerr.md)
  An error, such as a direction stack overflow,occurred in directionality processing.
- [var kTECGlobalsUnavailableErr: Int](ktecglobalsunavailableerr.md)
  Global variables have already been deallocated,premature termination. The function did not convert the string.
- [var kTECItemUnavailableErr: Int](ktecitemunavailableerr.md)
  An item (for example, a name) is not availablefor the specified region (and encoding, if relevant).
- [var kTECUsedFallbacksStatus: Int](ktecusedfallbacksstatus.md)
  The function has completely converted theinput string to the specified target using one or more fallbacks.For the Unicode Converter, this status code can only occur if the `kUnicodeUseFallbacksBit`control flag is set.
- [var kTECNeedFlushStatus: Int](ktecneedflushstatus.md)
  The application disposed of a converterobject by calling TECDisposeConverter, but there is still text containedin internal buffers. Returned by the Text Encoding Converter functionsonly. 
- [var kTECOutputBufferFullStatus: Int](ktecoutputbufferfullstatus.md)
  The converter successfully converted partof the input text, but the output buffer was not large enough toaccommodate the entire input text after conversion. Convert theremaining text beginning from the position where the conversion stopped. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/ktecnoconversionpatherr)*