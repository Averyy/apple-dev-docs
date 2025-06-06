# IOStreamBuffer

**Framework**: Kernel  
**Kind**: cl

A class representing a data buffer that is part of an IOStream.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IOStreamBuffer : OSObject
```

## Topics

### Miscellaneous
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
- [withMemoryDescriptors](iostreambuffer/1809743-withmemorydescriptors.md)
### Instance Methods
- [- free](iostreambuffer/1589842-free.md)
- [- getBufferID](iostreambuffer/1589865-getbufferid.md)
- [- getClientReferenceCount](iostreambuffer/1589848-getclientreferencecount.md)
- [- getControlBuffer](iostreambuffer/1589855-getcontrolbuffer.md)
- [- getDataBuffer](iostreambuffer/1589832-getdatabuffer.md)
- [- getMetaClass](iostreambuffer/1589860-getmetaclass.md)
- [- initWithMemoryDescriptors](iostreambuffer/1589849-initwithmemorydescriptors.md)
- [- receiveClientReference](iostreambuffer/1589850-receiveclientreference.md)
- [- sendClientReference](iostreambuffer/1589869-sendclientreference.md)
- [- setBufferID](iostreambuffer/1589859-setbufferid.md)
- [- setControlBuffer](iostreambuffer/1589875-setcontrolbuffer.md)
- [- setDataBuffer](iostreambuffer/1589857-setdatabuffer.md)
### Type Methods
- [+ withMemoryDescriptors](iostreambuffer/1589864-withmemorydescriptors.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOSharedDataQueue](ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](iosharedinterruptcontroller.md)
- [IOUserClient](iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStreamUserClient](iostreamuserclient.md)
- [IOStream](iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreambuffer)*