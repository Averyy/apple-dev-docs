# IOUserClient

**Framework**: Kernel  
**Kind**: cl

Provides a basis for communication between client applications and I/O Kit objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOUserClient : IOService
```

#### Overview

## Topics

### Miscellaneous
- [exportObjectToClient](iouserclient/1809421-exportobjecttoclient.md)
- [releaseAsyncReference64](iouserclient/1809435-releaseasyncreference64.md)
  Release the mach_port_t reference held within the OSAsyncReference64 structure.
- [releaseNotificationPort](iouserclient/1809442-releasenotificationport.md)
  Release the mach_port_t passed to registerNotificationPort().
- [removeMappingForDescriptor](iouserclient/1809451-removemappingfordescriptor.md)
- [sendAsyncResult64WithOptions](iouserclient/1809458-sendasyncresult64withoptions.md)
  Send a notification as with sendAsyncResult, but with finite queueing.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iouserclient/reserved.md)
### Instance Methods
- [- AsyncCompletion](iouserclient/3325802-asynccompletion.md)
- [- CopyClientEntitlements](iouserclient/3753507-copycliententitlements.md)
- [- CopyClientEntitlements_Impl](iouserclient/3753508-copycliententitlements_impl.md)
- [- CopyClientMemoryForType](iouserclient/3325804-copyclientmemoryfortype.md)
- [- CreateActionKernelCompletion](iouserclient/3325806-createactionkernelcompletion.md)
- [- CreateMemoryDescriptorFromClient](iouserclient/3674617-creatememorydescriptorfromclient.md)
- [- CreateMemoryDescriptorFromClient_Impl](iouserclient/3674618-creatememorydescriptorfromclient.md)
- [- Dispatch](iouserclient/3325807-dispatch.md)
- [- KernelCompletion_Impl](iouserclient/3325809-kernelcompletion_impl.md)
- [- clientClose](iouserclient/1400611-clientclose.md)
- [- clientDied](iouserclient/1400591-clientdied.md)
- [- clientMemoryForType](iouserclient/1400739-clientmemoryfortype.md)
- [- clientMemoryForType](iouserclient/3553394-clientmemoryfortype.md)
- [- connectClient](iouserclient/1400570-connectclient.md)
- [- exportObjectToClient](iouserclient/1400687-exportobjecttoclient.md)
- [- externalMethod](iouserclient/1400572-externalmethod.md)
- [- free](../driverkit/iouserclient/free.md)
- [- getAsyncTargetAndMethodForIndex](iouserclient/1400681-getasynctargetandmethodforindex.md)
- [- getAsyncTargetAndMethodForIndex](iouserclient/3553398-getasynctargetandmethodforindex.md)
- [- getExternalAsyncMethodForIndex](iouserclient/1400712-getexternalasyncmethodforindex.md)
- [- getExternalMethodForIndex](iouserclient/1400635-getexternalmethodforindex.md)
- [- getExternalTrapForIndex](iouserclient/1400744-getexternaltrapforindex.md)
- [- getMetaClass](iouserclient/1400689-getmetaclass.md)
- [- getNotificationSemaphore](iouserclient/1400718-getnotificationsemaphore.md)
- [- getService](iouserclient/1400589-getservice.md)
- [- getTargetAndMethodForIndex](iouserclient/1400581-gettargetandmethodforindex.md)
- [- getTargetAndMethodForIndex](iouserclient/3553399-gettargetandmethodforindex.md)
- [- getTargetAndTrapForIndex](iouserclient/1400685-gettargetandtrapforindex.md)
- [- init](../driverkit/iouserclient/init.md)
- [- init](iouserclient/3516501-init.md)
- [- initWithTask](iouserclient/1400644-initwithtask.md)
- [- initWithTask](iouserclient/3516502-initwithtask.md)
- [- registerNotificationPort](iouserclient/1400665-registernotificationport.md)
- [- registerNotificationPort](iouserclient/3516503-registernotificationport.md)
- [- removeMappingForDescriptor](iouserclient/1400609-removemappingfordescriptor.md)
- [- reserve](iouserclient/1400729-reserve.md)
### Type Methods
- [+ AsyncCompletion_Invoke](iouserclient/4520003-asynccompletion_invoke.md)
- [+ AsyncCompletion_Invoke](iouserclient/4520004-asynccompletion_invoke.md)
- [+ CopyClientEntitlements_Invoke](iouserclient/3753509-copycliententitlements_invoke.md)
- [+ CopyClientMemoryForType_Invoke](iouserclient/3325805-copyclientmemoryfortype_invoke.md)
- [+ CreateMemoryDescriptorFromClient_Invoke](iouserclient/3674619-creatememorydescriptorfromclient.md)
- [+ clientHasAuthorization](iouserclient/1400663-clienthasauthorization.md)
- [+ clientHasPrivilege](iouserclient/1400625-clienthasprivilege.md)
- [+ copyClientEntitlement](iouserclient/1400731-copycliententitlement.md)
- [+ copyClientEntitlementVnode](iouserclient/3553395-copycliententitlementvnode.md)
- [+ copyClientEntitlements](iouserclient/3230669-copycliententitlements.md)
- [+ copyClientEntitlementsVnode](iouserclient/3553396-copycliententitlementsvnode.md)
- [+ releaseAsyncReference64](iouserclient/1400558-releaseasyncreference64.md)
- [+ releaseNotificationPort](iouserclient/1400583-releasenotificationport.md)
- [+ sendAsyncResult](iouserclient/1400599-sendasyncresult.md)
- [+ sendAsyncResult64](iouserclient/1400605-sendasyncresult64.md)
- [+ sendAsyncResult64WithOptions](iouserclient/1400667-sendasyncresult64withoptions.md)
- [+ setAsyncReference](iouserclient/1400699-setasyncreference.md)
- [+ setAsyncReference64](iouserclient/1400633-setasyncreference64.md)
- [+ setAsyncReference64](iouserclient/3516504-setasyncreference64.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOSharedDataQueue](ioshareddataqueue.md)
  A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.
- [IOSharedInterruptController](iosharedinterruptcontroller.md)
- [IOStreamUserClient](iostreamuserclient.md)
- [IOStream](iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient)*