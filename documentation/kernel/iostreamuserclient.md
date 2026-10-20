# IOStreamUserClient

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.5+

## Declaration

```cpp
class IOStreamUserClient : IOUserClient
```

## Topics

### Instance Methods
- [- clientClose](./iostreamuserclient/api-1576514-clientclose.md)
- [- clientDied](./iostreamuserclient/api-1576503-clientdied.md)
- [- clientMemoryForType](./iostreamuserclient/api-1576515-clientmemoryfortype.md)
- [- clientMemoryForTypeGated](./iostreamuserclient/api-3684907-clientmemoryfortypegated.md)
- [- closeMethod](./iostreamuserclient/api-1576522-closemethod.md)
- [- connectClient](./iostreamuserclient/api-1576517-connectclient.md)
- [- free](./iostreamuserclient/api-3684908-free.md)
- [- getBufferCountMethod](./iostreamuserclient/api-1576511-getbuffercountmethod.md)
- [- getMetaClass](./iostreamuserclient/api-1576516-getmetaclass.md)
- [- getModeMethod](./iostreamuserclient/api-1576509-getmodemethod.md)
- [- getService](./iostreamuserclient/api-1576513-getservice.md)
- [- getTargetAndMethodForIndex](./iostreamuserclient/api-1576521-gettargetandmethodforindex.md)
- [- getTargetAndMethodForIndexGated](./iostreamuserclient/api-3684909-gettargetandmethodforindexgated.md)
- [- getTargetAndTrapForIndex](./iostreamuserclient/api-1576504-gettargetandtrapforindex.md)
- [- initWithTask](./iostreamuserclient/api-1576510-initwithtask.md)
- [- initWithTask](./iostreamuserclient/api-3516783-initwithtask.md)
- [- inputSyncTrap](./iostreamuserclient/api-1576518-inputsynctrap.md)
- [- inputTrap](./iostreamuserclient/api-1576520-inputtrap.md)
- [- openMethod](./iostreamuserclient/api-1576502-openmethod.md)
- [- registerNotificationPort](./iostreamuserclient/api-1576523-registernotificationport.md)
- [- setModeMethod](./iostreamuserclient/api-1576508-setmodemethod.md)
- [- start](./iostreamuserclient/api-1576512-start.md)
- [- startMethod](./iostreamuserclient/api-1576506-startmethod.md)
- [- stop](./iostreamuserclient/api-3684910-stop.md)
- [- stopMethod](./iostreamuserclient/api-1576519-stopmethod.md)
- [- suspendMethod](./iostreamuserclient/api-1576507-suspendmethod.md)

## Relationships

### Inherits From
- [IOUserClient](./iouserclient.md)

## See Also

### User-Space Interactions
- [IOSharedDataQueue](./ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](./iosharedinterruptcontroller.md)
- [IOUserClient](./iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStream](./iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](./iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](./osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](./osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iostreamuserclient)*