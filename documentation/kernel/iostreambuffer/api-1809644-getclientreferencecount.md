# getClientReferenceCount

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual SInt32 getClientReferenceCount(
 void );
```

#### Return Value

The count of client references to this buffer. It may be positive or negative, depending on whether the client is sending data into the kernel, or the kernel is sending data out to the client.

## See Also

### Miscellaneous
- [getBufferID](./api-1809634-getbufferid.md)
  Gets the buffer identifier for the IOStreamBuffer object.
- [getControlBuffer](./api-1809652-getcontrolbuffer.md)
- [getDataBuffer](./api-1809666-getdatabuffer.md)
- [initWithMemoryDescriptors](./api-1809676-initwithmemorydescriptors.md)
- [receiveClientReference](./api-1809687-receiveclientreference.md)
- [sendClientReference](./api-1809696-sendclientreference.md)
- [setBufferID](./api-1809706-setbufferid.md)
  Sets the buffer identifier for the IOStreamBuffer object.
- [setControlBuffer](./api-1809716-setcontrolbuffer.md)
  Sets the control buffer for the IOStreamBuffer object.
- [setDataBuffer](./api-1809732-setdatabuffer.md)
  Sets the data buffer for the IOStreamBuffer object.
- [withMemoryDescriptors](./api-1809743-withmemorydescriptors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambuffer/1809644-getclientreferencecount)*