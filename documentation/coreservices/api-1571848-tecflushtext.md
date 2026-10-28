# TECFlushText

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Flushes out any data in a converter object’s temporarybuffers and resets the converter object.

**Availability**:
- macOS 10.0+

## Declaration

```c
OSStatus TECFlushText(TECObjectRef encodingConverter, TextPtr outputBuffer, ByteCount outputBufferLength, ByteCount *actualOutputLength);
```

## Return Value

A resultcode. See [Result Codes](./carbon_core/text_encoding_conversion_manager.md#1664324).

## Discussion

You should always call `TECFlushText` whenyou finish converting a text stream. If you are converting a singlestream in multiple chunks using multiple calls to `TECConvertText`,you only need to call `TECFlushText` afterthe last call to `TECConvertText` forthat stream. The function uses the conversion path specified inthe converter object you supply. 

For the function to return successfully, the output bufferyou allocate must be large enough to accommodate the flushed text.If the output buffer is too small to accommodate any flushed text,the function will fail. For best results, you should follow theseguidelines when you allocate an output buffer:

-  Base the buffer length on an estimate of thebyte requirements of the destination encoding. Make sure you accountfor additional bytes needed by the destination encoding (for example,an escape sequence) in addition to the actual text.  
-  Always allocate a buffer at least 32 bytes long.  

Encodings such as ISO-2022 that need to shift back to a certaindefault state at the end of a conversion can do so when this functionis called. 

## Parameters

- `encodingConverter`: A reference to the text converter object whose contents are to be flushed. This can be a reference returned by the [`TECCreateConverter`](./api-1571815-teccreateconverter.md) or [`TECCreateConverterFromPath`](./api-1571829-teccreateconverterfrompath.md) functions. 
- `outputBuffer`: On return, a pointer to a buffer that holds the converted text. 
- `outputBufferLength`: The length in bytes of the buffer provided by the `outputBuffer` parameter. 
- `actualOutputLength`: On return, a pointer to the number of bytes of converted text returned in the buffer specified by the `outputBuffer` parameter.

## See Also

### Converting Text Between Encodings
- [TECConvertText](./api-1571824-tecconverttext.md)
  Converts a stream of text from a source encoding to adestination encoding. It uses the conversion path specified by theconverter object you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1571848-tecflushtext)*