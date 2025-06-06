# IOStreamUserClient

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IOStreamUserClient : IOUserClient
```

## Topics

### Instance Methods
- [- clientClose](iostreamuserclient/1576514-clientclose.md)
- [- clientDied](iostreamuserclient/1576503-clientdied.md)
- [- clientMemoryForType](iostreamuserclient/1576515-clientmemoryfortype.md)
- [- clientMemoryForTypeGated](iostreamuserclient/3684907-clientmemoryfortypegated.md)
- [- closeMethod](iostreamuserclient/1576522-closemethod.md)
- [- connectClient](iostreamuserclient/1576517-connectclient.md)
- [- free](iostreamuserclient/3684908-free.md)
- [- getBufferCountMethod](iostreamuserclient/1576511-getbuffercountmethod.md)
- [- getMetaClass](iostreamuserclient/1576516-getmetaclass.md)
- [- getModeMethod](iostreamuserclient/1576509-getmodemethod.md)
- [- getService](iostreamuserclient/1576513-getservice.md)
- [- getTargetAndMethodForIndex](iostreamuserclient/1576521-gettargetandmethodforindex.md)
- [- getTargetAndMethodForIndexGated](iostreamuserclient/3684909-gettargetandmethodforindexgated.md)
- [- getTargetAndTrapForIndex](iostreamuserclient/1576504-gettargetandtrapforindex.md)
- [- initWithTask](iostreamuserclient/1576510-initwithtask.md)
- [- initWithTask](iostreamuserclient/3516783-initwithtask.md)
- [- inputSyncTrap](iostreamuserclient/1576518-inputsynctrap.md)
- [- inputTrap](iostreamuserclient/1576520-inputtrap.md)
- [- openMethod](iostreamuserclient/1576502-openmethod.md)
- [- registerNotificationPort](iostreamuserclient/1576523-registernotificationport.md)
- [- setModeMethod](iostreamuserclient/1576508-setmodemethod.md)
- [- start](iostreamuserclient/1576512-start.md)
- [- startMethod](iostreamuserclient/1576506-startmethod.md)
- [- stop](iostreamuserclient/3684910-stop.md)
- [- stopMethod](iostreamuserclient/1576519-stopmethod.md)
- [- suspendMethod](iostreamuserclient/1576507-suspendmethod.md)

## Relationships

### Inherits From
- [IOUserClient](iouserclient.md)

## See Also

- [IOSharedDataQueue](ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](iosharedinterruptcontroller.md)
- [IOUserClient](iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStream](iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreamuserclient)*