# PassthruInterruptController

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class PassthruInterruptController : IOInterruptController
```

## Topics

### Instance Methods
- [- causeInterrupt](./passthruinterruptcontroller/api-3553401-causeinterrupt.md)
- [- disableInterrupt](./passthruinterruptcontroller/api-3553402-disableinterrupt.md)
- [- enableInterrupt](./passthruinterruptcontroller/api-3553403-enableinterrupt.md)
- [- externalInterrupt](./passthruinterruptcontroller/api-3553404-externalinterrupt.md)
- [- getInterruptType](./passthruinterruptcontroller/api-3553405-getinterrupttype.md)
- [- getMetaClass](./passthruinterruptcontroller/api-3553406-getmetaclass.md)
- [- handleInterrupt](./passthruinterruptcontroller/api-3553407-handleinterrupt.md)
- [- init](./passthruinterruptcontroller/api-3553408-init.md)
- [- registerInterrupt](./passthruinterruptcontroller/api-3553409-registerinterrupt.md)
- [- setCPUInterruptProperties](./passthruinterruptcontroller/api-3553410-setcpuinterruptproperties.md)
- [- waitForChildController](./passthruinterruptcontroller/api-3553411-waitforchildcontroller.md)

## Relationships

### Inherits From
- [IOInterruptController](./iointerruptcontroller.md)

## See Also

### Interrupts
- [IOInterruptDispatchSource](./iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](./iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](./iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptEventSource](./iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [IOInterruptController](./iointerruptcontroller.md)
- [IOInterruptSource](./iointerruptsource.md)
- [IOInterruptVector](./iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/passthruinterruptcontroller)*