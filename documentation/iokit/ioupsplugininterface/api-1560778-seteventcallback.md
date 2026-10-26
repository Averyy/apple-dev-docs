# setEventCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set the callback that should be called to handle an event from the UPS.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
IOReturn (*setEventCallback)(void *thisPointer, IOUPSEventCallbackFunction callback, void *callbackTarget, void *callbackRefcon);
```

#### Return Value

An IOReturn error code.

#### Discussion

The proivided callback method should be called whenever there is a change of state in the UPS. This should be used in conjunction with createAsyncEventSource.

## Parameters

- `thisPointer`: The UPS Interface to use.
- `callback`: A callback handler of type IOUPSEventCallbackFunction.
- `callbackTarget`: The address to be targeted by this callback.
- `callbackRefcon`: A user specified reference value. This will be passed to all callback functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugininterface/1560778-seteventcallback)*