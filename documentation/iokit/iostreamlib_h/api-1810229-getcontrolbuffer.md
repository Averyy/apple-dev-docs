# GetControlBuffer

**Framework**: IOKit  
**Kind**: func

Get a pointer to the control area of an IOStreamBuffer.

## Declaration

```c
void *( *GetControlBuffer)(
   IOStreamRef stream,
   IOStreamBufferID bufferID );
```

#### Return Value

A pointer to the control buffer area of the IOStreamBuffer, or NULL if it does not have a control buffer.

## Parameters

- `stream`: The IOStreamRef of the stream owning the buffer.
- `bufferID`: The IOStreamBufferID of the buffer to operate on.

## See Also

### Buffer convenience functions
- [GetControlBufferLength](./api-1810244-getcontrolbufferlength.md)
  Get the length of the control area of an IOStreamBuffer.
- [GetDataBuffer](./api-1810262-getdatabuffer.md)
  Get a pointer to the data area of an IOStreamBuffer.
- [GetDataBufferLength](./api-1810274-getdatabufferlength.md)
  Get the length of the data area of an IOStreamBuffer.
- [GetMode](./api-1810285-getmode.md)
- [SetMode](./api-1810307-setmode.md)
- [StartStream](./api-1810318-startstream.md)
- [StopStream](./api-1810328-stopstream.md)
- [SuspendStream](./api-1810341-suspendstream.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iostreamlib_h/1810229-getcontrolbuffer)*