# IOInterruptVector

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOInterruptVector {
    ...
} IOInterruptVector;
```

## Topics

### Instance Properties
- [handler](./iointerruptvector/api-1420579-handler.md)
- [interruptActive](./iointerruptvector/api-1420606-interruptactive.md)
- [interruptDisabledHard](./iointerruptvector/api-1420584-interruptdisabledhard.md)
- [interruptDisabledSoft](./iointerruptvector/api-1420555-interruptdisabledsoft.md)
- [interruptLock](./iointerruptvector/api-1420548-interruptlock.md)
- [interruptRegistered](./iointerruptvector/api-1420599-interruptregistered.md)
- [nub](./iointerruptvector/api-1420590-nub.md)
- [refCon](./iointerruptvector/api-1420570-refcon.md)
- [sharedController](./iointerruptvector/api-1420588-sharedcontroller.md)
- [source](./iointerruptvector/api-1420542-source.md)
- [target](./iointerruptvector/api-1420604-target.md)

## See Also

### Interrupts
- [IOInterruptDispatchSource](./iointerruptdispatchsource.md)
- [IOInterruptDispatchSourceInterface](./iointerruptdispatchsourceinterface.md)
- [IOFilterInterruptEventSource](./iofilterinterrupteventsource.md)
  Filtering varient of the $link IOInterruptEventSource.
- [IOInterruptEventSource](./iointerrupteventsource.md)
  Event source for interrupt delivery to work-loop based drivers.
- [IOInterruptController](./iointerruptcontroller.md)
- [PassthruInterruptController](./passthruinterruptcontroller.md)
- [IOInterruptSource](./iointerruptsource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerruptvector)*