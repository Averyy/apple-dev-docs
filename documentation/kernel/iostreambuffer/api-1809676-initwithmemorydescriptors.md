# initWithMemoryDescriptors

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual bool initWithMemoryDescriptors(
 IOMemoryDescriptor *dataBuffer, 
 IOMemoryDescriptor *controlBuffer, 
 IOStreamBufferID bufferID = 0);
```

## See Also

### Miscellaneous
- [getBufferID](./api-1809634-getbufferid.md)
  Gets the buffer identifier for the IOStreamBuffer object.
- [getClientReferenceCount](./api-1809644-getclientreferencecount.md)
- [getControlBuffer](./api-1809652-getcontrolbuffer.md)
- [getDataBuffer](./api-1809666-getdatabuffer.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambuffer/1809676-initwithmemorydescriptors)*