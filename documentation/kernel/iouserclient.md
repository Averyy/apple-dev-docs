# IOUserClient

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Provides a basis for communication between client applications and I/O Kit objects.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOUserClient : IOService
```

## Overview

## Topics

### Miscellaneous
- [exportObjectToClient](./iouserclient/api-1809421-exportobjecttoclient.md)
- [releaseAsyncReference64](./iouserclient/api-1809435-releaseasyncreference64.md)
  Release the mach_port_t reference held within the OSAsyncReference64 structure.
- [releaseNotificationPort](./iouserclient/api-1809442-releasenotificationport.md)
  Release the mach_port_t passed to registerNotificationPort().
- [removeMappingForDescriptor](./iouserclient/api-1809451-removemappingfordescriptor.md)
- [sendAsyncResult64WithOptions](./iouserclient/api-1809458-sendasyncresult64withoptions.md)
  Send a notification as with sendAsyncResult, but with finite queueing.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iouserclient/reserved.md)
### Instance Methods
- [- AsyncCompletion](./iouserclient/api-3325802-asynccompletion.md)
- [- CopyClientEntitlements](./iouserclient/api-3753507-copycliententitlements.md)
- [- CopyClientEntitlements_Impl](./iouserclient/api-3753508-copycliententitlements_impl.md)
- [- CopyClientMemoryForType](./iouserclient/api-3325804-copyclientmemoryfortype.md)
- [- CreateActionKernelCompletion](./iouserclient/api-3325806-createactionkernelcompletion.md)
- [- CreateMemoryDescriptorFromClient](./iouserclient/api-3674617-creatememorydescriptorfromclient.md)
- [- CreateMemoryDescriptorFromClient_Impl](./iouserclient/api-3674618-creatememorydescriptorfromclient.md)
- [- Dispatch](./iouserclient/api-3325807-dispatch.md)
- [- KernelCompletion_Impl](./iouserclient/api-3325809-kernelcompletion_impl.md)
- [- clientClose](./iouserclient/api-1400611-clientclose.md)
- [- clientDied](./iouserclient/api-1400591-clientdied.md)
- [- clientMemoryForType](./iouserclient/api-1400739-clientmemoryfortype.md)
- [- clientMemoryForType](./iouserclient/api-3553394-clientmemoryfortype.md)
- [- connectClient](./iouserclient/api-1400570-connectclient.md)
- [- exportObjectToClient](./iouserclient/api-1400687-exportobjecttoclient.md)
- [- externalMethod](./iouserclient/api-1400572-externalmethod.md)
- [- free](./iouserclient/api-3325622-free.md)
- [- getAsyncTargetAndMethodForIndex](./iouserclient/api-1400681-getasynctargetandmethodforindex.md)
- [- getAsyncTargetAndMethodForIndex](./iouserclient/api-3553398-getasynctargetandmethodforindex.md)
- [- getExternalAsyncMethodForIndex](./iouserclient/api-1400712-getexternalasyncmethodforindex.md)
- [- getExternalMethodForIndex](./iouserclient/api-1400635-getexternalmethodforindex.md)
- [- getExternalTrapForIndex](./iouserclient/api-1400744-getexternaltrapforindex.md)
- [- getMetaClass](./iouserclient/api-1400689-getmetaclass.md)
- [- getNotificationSemaphore](./iouserclient/api-1400718-getnotificationsemaphore.md)
- [- getService](./iouserclient/api-1400589-getservice.md)
- [- getTargetAndMethodForIndex](./iouserclient/api-1400581-gettargetandmethodforindex.md)
- [- getTargetAndMethodForIndex](./iouserclient/api-3553399-gettargetandmethodforindex.md)
- [- getTargetAndTrapForIndex](./iouserclient/api-1400685-gettargetandtrapforindex.md)
- [- init](./iouserclient/api-3325623-init.md)
- [- init](./iouserclient/api-3516501-init.md)
- [- initWithTask](./iouserclient/api-1400644-initwithtask.md)
- [- initWithTask](./iouserclient/api-3516502-initwithtask.md)
- [- registerNotificationPort](./iouserclient/api-1400665-registernotificationport.md)
- [- registerNotificationPort](./iouserclient/api-3516503-registernotificationport.md)
- [- removeMappingForDescriptor](./iouserclient/api-1400609-removemappingfordescriptor.md)
- [- reserve](./iouserclient/api-1400729-reserve.md)
### Type Methods
- [+ AsyncCompletion_Invoke](./iouserclient/api-4520003-asynccompletion_invoke.md)
- [+ AsyncCompletion_Invoke](./iouserclient/api-4520004-asynccompletion_invoke.md)
- [+ CopyClientEntitlements_Invoke](./iouserclient/api-3753509-copycliententitlements_invoke.md)
- [+ CopyClientMemoryForType_Invoke](./iouserclient/api-3325805-copyclientmemoryfortype_invoke.md)
- [+ CreateMemoryDescriptorFromClient_Invoke](./iouserclient/api-3674619-creatememorydescriptorfromclient.md)
- [+ clientHasAuthorization](./iouserclient/api-1400663-clienthasauthorization.md)
- [+ clientHasPrivilege](./iouserclient/api-1400625-clienthasprivilege.md)
- [+ copyClientEntitlement](./iouserclient/api-1400731-copycliententitlement.md)
- [+ copyClientEntitlementVnode](./iouserclient/api-3553395-copycliententitlementvnode.md)
- [+ copyClientEntitlements](./iouserclient/api-3230669-copycliententitlements.md)
- [+ copyClientEntitlementsVnode](./iouserclient/api-3553396-copycliententitlementsvnode.md)
- [+ releaseAsyncReference64](./iouserclient/api-1400558-releaseasyncreference64.md)
- [+ releaseNotificationPort](./iouserclient/api-1400583-releasenotificationport.md)
- [+ sendAsyncResult](./iouserclient/api-1400599-sendasyncresult.md)
- [+ sendAsyncResult64](./iouserclient/api-1400605-sendasyncresult64.md)
- [+ sendAsyncResult64WithOptions](./iouserclient/api-1400667-sendasyncresult64withoptions.md)
- [+ setAsyncReference](./iouserclient/api-1400699-setasyncreference.md)
- [+ setAsyncReference64](./iouserclient/api-1400633-setasyncreference64.md)
- [+ setAsyncReference64](./iouserclient/api-3516504-setasyncreference64.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### User-Space Interactions
- [IOSharedDataQueue](./ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](./iosharedinterruptcontroller.md)
- [IOStreamUserClient](./iostreamuserclient.md)
- [IOStream](./iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](./iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](./osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](./osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient)*