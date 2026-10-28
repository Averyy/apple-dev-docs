# setMessageCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set callback for user space message routine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setMessageCallback)(void *self, void *refCon, IOFWSBP2MessageCallback callback);
```

## Discussion

In FireWire & SBP2 bus status messages are delivered via IOKit's message routine. This routine is emulated in user space for SBP2 & FireWire messages via this callback. You should register here for bus reset, and reconnect messages.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.
- `refCon`: RefCon to be returned as first argument of completion routine
- `callback`: Address of completion routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590467-setmessagecallback)*