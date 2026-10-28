# GetBufferInfo

**Framework**: IOKit  
**Kind**: func

Gets information about a buffer in an IOStream.

## Declaration

```c
IOReturn ( *GetBufferInfo)(
   IOStreamRef stream,
   IOStreamBufferID bufferID,
   void **dataBufferAddressOut,
   IOByteCount *dataBufferSizeOut,
   void **controlBufferAddressOut,
   IOByteCount *controlBufferSizeOut );
```

## Return Value

Returns kIOReturnSuccess if the buffer ID was valid.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.
- `bufferID`: 
- `dataBufferAddressOut`: 
- `dataBufferSizeOut`: 
- `controlBufferAddressOut`: 
- `controlBufferSizeOut`: 

## See Also

### Buffer information
- [GetBufferCount](./api-1810203-getbuffercount.md)
  Gets the number of buffers in the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810214-getbufferinfo)*