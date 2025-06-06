# IOSharedInterruptController

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOSharedInterruptController : IOInterruptController
```

## Topics

### Instance Methods
- [- disableInterrupt](iosharedinterruptcontroller/1420608-disableinterrupt.md)
- [- enableInterrupt](iosharedinterruptcontroller/1420546-enableinterrupt.md)
- [- getInterruptHandlerAddress](iosharedinterruptcontroller/1420566-getinterrupthandleraddress.md)
- [- getInterruptType](iosharedinterruptcontroller/1420534-getinterrupttype.md)
- [- getMetaClass](iosharedinterruptcontroller/1420538-getmetaclass.md)
- [- handleInterrupt](iosharedinterruptcontroller/1420568-handleinterrupt.md)
- [- initInterruptController](iosharedinterruptcontroller/1420540-initinterruptcontroller.md)
- [- registerInterrupt](iosharedinterruptcontroller/1420532-registerinterrupt.md)
- [- unregisterInterrupt](iosharedinterruptcontroller/1420559-unregisterinterrupt.md)

## Relationships

### Inherits From
- [IOInterruptController](iointerruptcontroller.md)

## See Also

- [IOSharedDataQueue](ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOUserClient](iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStreamUserClient](iostreamuserclient.md)
- [IOStream](iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iosharedinterruptcontroller)*