# TECConvertText

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Converts a stream of text from a source encoding to adestination encoding. It uses the conversion path specified by theconverter object you supply.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECConvertText(TECObjectRef encodingConverter, ConstTextPtr inputBuffer, ByteCount inputBufferLength, ByteCount *actualInputLength, TextPtr outputBuffer, ByteCount outputBufferLength, ByteCount *actualOutputLength);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324). If there is not enough memoryavailable for `TECConvertText` toconvert the text when allocating internal buffers, the functionreturns the appropriate Memory Manager result code.

In most cases, `TECConvertText` does not return [`kTECUsedFallbacksStatus`](./api-1560006-anonymous/ktecusedfallbacksstatus.md) even if it has substituted a fallback character in the process of converting its input text to output in another encoding (unlike, for example, [`ConvertFromUnicodeToText`](./api-1433542-convertfromunicodetotext.md) which always returns [`kTECUsedFallbacksStatus`](./api-1560006-anonymous/ktecusedfallbacksstatus.md) if it substitutes a fallback character). That is because `TECConvertText` is intended to be used primarily by clients who just want it to do the best job it can in converting from a given input encoding to a given output encoding and don't want to worry too much about the details.

## Discussion

If the output buffer you allocate is too small to accommodateany of the converted text, the function fails. For best results,you should follow these guidelines when you allocate an output buffer:

- Base the buffer length on an estimate of thebyte requirements of the destination encoding. Make sure you accountfor additional bytes needed by the destination encoding (for example,an escape sequence) in addition to the actual text.  
-  Always allocate a buffer at least 32 bytes long.  
-  If size is a concern, make sure the output buffer is at leastlarge enough to hold a portion of the converted text. You can convertpart of the text, then use the value of the `actualInputLength` parameterto identify the next byte to be taken and to determine how manybytes remain. To convert the remaining text, you simply call thefunction again with the remaining text and a new output buffer. 
-  If the destination encoding is a character encoding scheme—suchas ISO-2022-JP, which begins in ASCII and switches to other codedcharacter sets through limited combinations of escape sequences—thenyou need to allocate enough space to accommodate escape sequencesthat signal switches. ISO-2022-JP requires 3 to 5 bytes for an escapesequence preceding the 1-byte or 2-byte character it introduces.If you allocate a buffer that is less than 5 bytes, the TECConvertTextfunction could fail, depending on the text being converted.  

To make sure that you receive all of the converted text, youshould call the function  [`TECFlushText`](./api-1571848-tecflushtext.md) when you are finished converting all the text in a text stream. 

## Parameters

- `encodingConverter`: A reference to the text encoding converter object you want to use for the conversion. It can be a reference returned by the [`TECCreateConverter`](./api-1571815-teccreateconverter.md) or [`TECCreateConverterFromPath`](./api-1571829-teccreateconverterfrompath.md) functions. 
- `inputBuffer`: The stream of text you want to convert. 
- `inputBufferLength`: The length in bytes (`UInt8` or `unsigned char`) of the stream of text. 
- `actualInputLength`: On return, a pointer to the number of source text bytes that were converted from the input buffer.
- `outputBuffer`: A pointer to a buffer for a byte stream. On output, the buffer holds the converted text.
- `outputBufferLength`: The length in bytes of the `outputBuffer` parameter.
- `actualOutputLength`: On return, a pointer to the number of bytes of converted text returned in the `outputBuffer` parameter.

## See Also

### Converting Text Between Encodings
- [TECFlushText](./api-1571848-tecflushtext.md)
  Flushes out any data in a converter object’s temporarybuffers and resets the converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571824-tecconverttext)*