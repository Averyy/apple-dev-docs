# TECFlushMultipleEncodings

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Flushes out any encodings that may be stored in a converterobject’s temporary buffers and shifts encodings back to theirdefault state, if any.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECFlushMultipleEncodings(TECObjectRef encodingConverter, TextPtr outputBuffer, ByteCount outputBufferLength, ByteCount *actualOutputLength, TextEncodingRun outEncodingsBuffer[], ItemCount maxOutEncodingRuns, ItemCount *actualOutEncodingRuns);
```

#### Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

#### Discussion

You should always call `TECFlushMultipleEncodings` atthe end of the conversion process to flush out any data that maybe stored in the temporary buffers of the text encoding converterobject or to perform other end-of-encoding conversion tasks. Encodingssuch as ISO-2022-JP are reset to a default state when you use thisfunction. 

For the function to return successfully, the output bufferyou allocate must be large enough to accommodate the converted text.If the output buffer is too small to accommodate any converted text,the function will fail. For best results, you should follow theseguidelines when you allocate an output buffer:

-  Base the buffer length on an estimate of thebyte requirements of the destination encoding. Make sure you accountfor additional bytes needed by the destination encoding (for example,an escape sequence) in addition to the actual text.  
-  Always allocate a buffer at least 32 bytes long. 
-  If size is a concern, make sure the output buffer is at leastlarge enough to hold a portion of the converted text. You can convertpart of the text, then use the value of the `actualInputLength` parameterto identify the next byte to be taken and to determine how manybytes remain. To convert the remaining text, you simply call thefunction again with the remaining text and a new output buffer. 
-  If the destination encoding is a character encoding scheme—suchas ISO-2022-JP, which begins in ASCII and switches to other codedcharacter sets through limited combinations of escape sequences—thenyou need to allocate enough space to accommodate escape sequencesthat signal switches. ISO-2022-JP requires 3 to 5 bytes for an escapesequence preceding the 1-byte or 2-byte character it introduces.If you allocate a buffer that is less than 5 bytes, the `TECConvertText` functioncould fail, depending on the text being converted.  

## Parameters

- `encodingConverter`: The reference to the text encoding converter object whose contents are to be flushed. This is the reference returned by the function [`TECCreateOneToManyConverter`](./api-1571794-teccreateonetomanyconverter.md). 
- `outputBuffer`: On return, a pointer to a buffer that holds the converted text. An error is returned is the buffer is not large enough to hold the entire converted text stream. 
- `outputBufferLength`: The length in bytes of the `outputBuffer` parameter. 
- `actualOutputLength`: On return, a pointer to a the actual number of bytes of the converted text returned in the `outputBuffer` parameter.
- `outEncodingsBuffer`: An ordered array of text encoding runs for the destination text encoding. Note that the actual byte size of this buffer should be `actualOutEncodingRuns* sizeof(TextEncodingRun)`. 
- `maxOutEncodingRuns`: The maximum number of encoding runs that can fit in `outEncodingsBuffer`[]. 
- `actualOutEncodingRuns`: On return, a pointer to a the number of runs in the buffer during conversion.

## See Also

### Converting to Multiple Encoding Runs
- [TECConvertTextToMultipleEncodings](./api-1571849-tecconverttexttomultipleencoding.md)
  Converts text in the source encoding to runs of text inmultiple destination encodings. It uses the conversion path specifiedin the converter object you supply.
- [TECCreateOneToManyConverter](./api-1571794-teccreateonetomanyconverter.md)
  Determines a conversion path for the source encoding anddestinations encodings you specify, creates a text encoding converterobject, and returns a reference to it. 
- [TECGetEncodingList](./api-1571830-tecgetencodinglist.md)
  Gets the list of destination encodings from a converterobject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571842-tecflushmultipleencodings)*