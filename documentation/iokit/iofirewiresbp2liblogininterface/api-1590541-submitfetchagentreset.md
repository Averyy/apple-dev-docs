# submitFetchAgentReset

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Resets the LUN's fetch agent.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*submitFetchAgentReset)(void *self);
```

## Return Value

Returns kIOReturnSuccess if the reset started successfully.

## Discussion

The fetch agent state machine on the device can be reset by a write to a specific register. This reset can be intiated by a call to this method. Notification of the completion of this write can be had by registering a callback with the setFetchAgentResetCallback method.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590541-submitfetchagentreset)*