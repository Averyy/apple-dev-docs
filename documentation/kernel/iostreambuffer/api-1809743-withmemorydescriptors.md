# withMemoryDescriptors

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
static IOStreamBuffer *withMemoryDescriptors(
 IOMemoryDescriptor *dataBuffer, 
 IOMemoryDescriptor *controlBuffer, 
 IOStreamBufferID bufferID = 0);
```

## See Also

- [getBufferID](iostreambuffer/1809634-getbufferid.md)
  Gets the buffer identifier for the IOStreamBuffer object.
- [getClientReferenceCount](iostreambuffer/1809644-getclientreferencecount.md)
- [getControlBuffer](iostreambuffer/1809652-getcontrolbuffer.md)
- [getDataBuffer](iostreambuffer/1809666-getdatabuffer.md)
- [initWithMemoryDescriptors](iostreambuffer/1809676-initwithmemorydescriptors.md)
- [receiveClientReference](iostreambuffer/1809687-receiveclientreference.md)
- [sendClientReference](iostreambuffer/1809696-sendclientreference.md)
- [setBufferID](iostreambuffer/1809706-setbufferid.md)
  Sets the buffer identifier for the IOStreamBuffer object.
- [setControlBuffer](iostreambuffer/1809716-setcontrolbuffer.md)
  Sets the control buffer for the IOStreamBuffer object.
- [setDataBuffer](iostreambuffer/1809732-setdatabuffer.md)
  Sets the data buffer for the IOStreamBuffer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambuffer/1809743-withmemorydescriptors)*