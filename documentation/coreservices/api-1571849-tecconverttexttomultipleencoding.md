# TECConvertTextToMultipleEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts text in the source encoding to runs of text inmultiple destination encodings. It uses the conversion path specifiedin the converter object you supply.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECConvertTextToMultipleEncodings(TECObjectRef encodingConverter, ConstTextPtr inputBuffer, ByteCount inputBufferLength, ByteCount *actualInputLength, TextPtr outputBuffer, ByteCount outputBufferLength, ByteCount *actualOutputLength, TextEncodingRun outEncodingsBuffer[], ItemCount maxOutEncodingRuns, ItemCount *actualOutEncodingRuns);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). If there is not enough memoryavailable to convert the text when allocating internal buffers,the function returns the appropriate Memory Manager result code.

#### Discussion

For the function to return successfully, the output bufferyou allocate must be large enough to accommodate the converted text.If the output buffer is too small to accommodate any converted text,the function will fail. For best results, you should follow theseguidelines when you allocate an output buffer:

-  Base the buffer length on an estimate of thebyte requirements of the destination encoding. Make sure you accountfor additional bytes needed by the destination encoding (for example,an escape sequence) in addition to the actual text.  
-  Always allocate a buffer at least 32 bytes long. 
-  If size is a concern, make sure the output buffer is at leastlarge enough to hold a portion of the converted text. You can convertpart of the text, then use the value of the `actualInputLength` parameterto identify the next byte to be taken and to determine how manybytes remain. To convert the remaining text, you simply call thefunction again with the remaining text and a new output buffer. 
-  If the destination encoding is a character encoding scheme—suchas ISO-2022-JP, which begins in ASCII and switches to other codedcharacter sets through limited combinations of escape sequences—thenyou need to allocate enough space to accommodate escape sequencesthat signal switches. ISO-2022-JP requires 3 to 5 bytes for an escapesequence preceding the 1-byte or 2-byte character it introduces.If you allocate a buffer that is less than 5 bytes, the `TECConvertText` functioncould fail, depending on the text being converted.  

The Text Encoding Converter creates internal buffers thathold intermediate results for indirect conversions  

## Parameters

- `encodingConverter`: The reference to the text encoding converter object to be used for the conversion. This is the reference returned by the function [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md). 
- `inputBuffer`: The stream of text to be converted. 
- `inputBufferLength`: The length in bytes of the stream of text specified in the `inputBuffer` parameter. 
- `actualInputLength`: On return, a pointer to a the number of source text bytes that were converted.
- `outputBuffer`: On return, a pointer to a buffer that holds the converted text. 
- `outputBufferLength`: The length in bytes of the `outputBuffer` parameter.
- `actualOutputLength`: On return, a pointer to the number of bytes of the converted text returned in the `outputBuffer` parameter.
- `outEncodingsBuffer`: An array of text encoding runs for output. Note that the actual byte size of this buffer should be `actualOutEncodingRuns* sizeof(TextEncodingRun)`. 
- `maxOutEncodingRuns`: The maximum number of runs that can fit in the `outEncodingsBuffer` array. 
- `actualOutEncodingRuns`: On return, a pointer to the number of runs in `outEncodingsBuffer` array.

## See Also

### Converting to Multiple Encoding Runs
- [TECCreateOneToManyConverter](./api-1571794-teccreateonetomanyconverter.md)
  Determines a conversion path for the source encoding anddestinations encodings you specify, creates a text encoding converterobject, and returns a reference to it. 
- [TECFlushMultipleEncodings](./api-1571842-tecflushmultipleencodings.md)
  Flushes out any encodings that may be stored in a converterobject’s temporary buffers and shifts encodings back to theirdefault state, if any.
- [TECGetEncodingList](./api-1571830-tecgetencodinglist.md)
  Gets the list of destination encodings from a converterobject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571849-tecconverttexttomultipleencoding)*