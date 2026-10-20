# IOInterruptController

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOInterruptController : IOService
```

## Topics

### Instance Methods
- [- cancelDeferredIPI](./iointerruptcontroller/api-3553355-canceldeferredipi.md)
- [- causeInterrupt](./iointerruptcontroller/api-1420577-causeinterrupt.md)
- [- causeVector](./iointerruptcontroller/api-1420557-causevector.md)
- [- disableInterrupt](./iointerruptcontroller/api-1420602-disableinterrupt.md)
- [- disableVectorHard](./iointerruptcontroller/api-1420536-disablevectorhard.md)
- [- enableInterrupt](./iointerruptcontroller/api-1420595-enableinterrupt.md)
- [- enableVector](./iointerruptcontroller/api-1420593-enablevector.md)
- [- getInterruptHandlerAddress](./iointerruptcontroller/api-1420544-getinterrupthandleraddress.md)
- [- getInterruptType](./iointerruptcontroller/api-1420575-getinterrupttype.md)
- [- getMetaClass](./iointerruptcontroller/api-1420530-getmetaclass.md)
- [- getVectorType](./iointerruptcontroller/api-1420551-getvectortype.md)
- [- handleInterrupt](./iointerruptcontroller/api-1420553-handleinterrupt.md)
- [- initVector](./iointerruptcontroller/api-1420561-initvector.md)
- [- registerInterrupt](./iointerruptcontroller/api-1420528-registerinterrupt.md)
- [- sendIPI](./iointerruptcontroller/api-3553356-sendipi.md)
- [- setCPUInterruptProperties](./iointerruptcontroller/api-3553357-setcpuinterruptproperties.md)
- [- timeStampInterruptHandlerEnd](./iointerruptcontroller/api-2870514-timestampinterrupthandlerend.md)
- [- timeStampInterruptHandlerInternal](./iointerruptcontroller/api-2870517-timestampinterrupthandlerinterna.md)
- [- timeStampInterruptHandlerStart](./iointerruptcontroller/api-2870515-timestampinterrupthandlerstart.md)
- [- timeStampSpuriousInterrupt](./iointerruptcontroller/api-2870516-timestampspuriousinterrupt.md)
- [- unregisterInterrupt](./iointerruptcontroller/api-1420562-unregisterinterrupt.md)
- [- vectorCanBeShared](./iointerruptcontroller/api-1420582-vectorcanbeshared.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Interrupts
- [IOInterruptDispatchSource](./iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](./iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](./iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptEventSource](./iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [PassthruInterruptController](./passthruinterruptcontroller.md)
- [IOInterruptSource](./iointerruptsource.md)
- [IOInterruptVector](./iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerruptcontroller)*