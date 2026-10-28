# sendClientReference

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual SInt32 sendClientReference(
 IOByteCount offset = 0,
 IOByteCount length = 0 );
```

## Return Value

The new client reference count.

## Parameters

- `offset`: The offset in the buffer of the data sent to the client.
- `length`: The length of the data sent to the client.

## See Also

### Miscellaneous
- [getBufferID](./api-1809634-getbufferid.md)
  Gets the buffer identifier for the IOStreamBuffer object.
- [getClientReferenceCount](./api-1809644-getclientreferencecount.md)
- [getControlBuffer](./api-1809652-getcontrolbuffer.md)
- [getDataBuffer](./api-1809666-getdatabuffer.md)
- [initWithMemoryDescriptors](./api-1809676-initwithmemorydescriptors.md)
- [receiveClientReference](./api-1809687-receiveclientreference.md)
- [setBufferID](./api-1809706-setbufferid.md)
  Sets the buffer identifier for the IOStreamBuffer object.
- [setControlBuffer](./api-1809716-setcontrolbuffer.md)
  Sets the control buffer for the IOStreamBuffer object.
- [setDataBuffer](./api-1809732-setdatabuffer.md)
  Sets the data buffer for the IOStreamBuffer object.
- [withMemoryDescriptors](./api-1809743-withmemorydescriptors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambuffer/1809696-sendclientreference)*