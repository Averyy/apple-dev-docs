# removeCallbackDispatcherFromRunLoop

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Removes a dispatcher for kernel callbacks from the specified runloop.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*removeCallbackDispatcherFromRunLoop)(void *self);
```

#### Discussion

Undoes the work of addCallbackDispatcherToRunLoop.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590424-removecallbackdispatcherfromrunl)*