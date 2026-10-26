# removeCallbackDispatcherFromRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Removes a dispatcher for kernel callbacks to the specified run loop.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
void (*removeCallbackDispatcherFromRunLoop)(void *self);
```

#### Discussion

Undoes the work of addCallbackDispatcherToRunLoop.

## Parameters

- `self`: Pointer to IOFireWireAVCLibUnitInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508842-removecallbackdispatcherfromrunl)*