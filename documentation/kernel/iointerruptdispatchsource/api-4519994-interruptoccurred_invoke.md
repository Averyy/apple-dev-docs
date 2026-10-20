# InterruptOccurred_Invoke

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 15.4+

## Declaration

```c
static kern_return_t InterruptOccurred_Invoke(const IORPC rpc, OSMetaClassBase *target, InterruptOccurred_Handler func, const OSMetaClass *targetActionClass);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iointerruptdispatchsource/4519994-interruptoccurred_invoke)*