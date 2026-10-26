# GetBufferCount

**Framework**: IOKit  
**Kind**: func

Gets the number of buffers in the stream.

## Declaration

```c
IOItemCount ( *GetBufferCount)(
   IOStreamRef stream );
```

#### Return Value

Returns then number of buffers in the stream.

## Parameters

- `stream`: The IOStreamRef of the stream to operate on.

## See Also

### Buffer information
- [GetBufferInfo](./api-1810214-getbufferinfo.md)
  Gets information about a buffer in an IOStream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810203-getbuffercount)*