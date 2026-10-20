# IOInterruptSource

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef struct IOInterruptSource {
    ...
} IOInterruptSource;
```

## Topics

### Instance Properties
- [interruptController](./iointerruptsource/api-1400897-interruptcontroller.md)
- [vectorData](./iointerruptsource/api-1400895-vectordata.md)

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
- [IOInterruptVector](./iointerruptvector.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerruptsource)*