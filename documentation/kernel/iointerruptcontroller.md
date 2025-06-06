# IOInterruptController

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOInterruptController : IOService
```

## Topics

### Instance Methods
- [- cancelDeferredIPI](iointerruptcontroller/3553355-canceldeferredipi.md)
- [- causeInterrupt](iointerruptcontroller/1420577-causeinterrupt.md)
- [- causeVector](iointerruptcontroller/1420557-causevector.md)
- [- disableInterrupt](iointerruptcontroller/1420602-disableinterrupt.md)
- [- disableVectorHard](iointerruptcontroller/1420536-disablevectorhard.md)
- [- enableInterrupt](iointerruptcontroller/1420595-enableinterrupt.md)
- [- enableVector](iointerruptcontroller/1420593-enablevector.md)
- [- getInterruptHandlerAddress](iointerruptcontroller/1420544-getinterrupthandleraddress.md)
- [- getInterruptType](iointerruptcontroller/1420575-getinterrupttype.md)
- [- getMetaClass](iointerruptcontroller/1420530-getmetaclass.md)
- [- getVectorType](iointerruptcontroller/1420551-getvectortype.md)
- [- handleInterrupt](iointerruptcontroller/1420553-handleinterrupt.md)
- [- initVector](iointerruptcontroller/1420561-initvector.md)
- [- registerInterrupt](iointerruptcontroller/1420528-registerinterrupt.md)
- [- sendIPI](iointerruptcontroller/3553356-sendipi.md)
- [- setCPUInterruptProperties](iointerruptcontroller/3553357-setcpuinterruptproperties.md)
- [- timeStampInterruptHandlerEnd](iointerruptcontroller/2870514-timestampinterrupthandlerend.md)
- [- timeStampInterruptHandlerInternal](iointerruptcontroller/2870517-timestampinterrupthandlerinterna.md)
- [- timeStampInterruptHandlerStart](iointerruptcontroller/2870515-timestampinterrupthandlerstart.md)
- [- timeStampSpuriousInterrupt](iointerruptcontroller/2870516-timestampspuriousinterrupt.md)
- [- unregisterInterrupt](iointerruptcontroller/1420562-unregisterinterrupt.md)
- [- vectorCanBeShared](iointerruptcontroller/1420582-vectorcanbeshared.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOInterruptDispatchSource](iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptEventSource](iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [PassthruInterruptController](passthruinterruptcontroller.md)
- [IOInterruptSource](iointerruptsource.md)
- [IOInterruptVector](iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerruptcontroller)*