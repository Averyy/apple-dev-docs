# registerInterrupt

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 11.0+

## Declaration

```cpp
virtual IOReturn registerInterrupt(IOService *nub, int source, void *target, IOInterruptHandler handler, void *refCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/passthruinterruptcontroller/3553409-registerinterrupt)*