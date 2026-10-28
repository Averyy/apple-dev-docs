# enableUnsolicitedStatus

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Enables unsolicited status.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*enableUnsolicitedStatus)(void *self);
```

## Return Value

Returns kIOReturnSuccess if the status enable write started successfully.

## Discussion

After unsolicited is sent the device will not send any additional unsolicited status until a specific register is written. This serves as a sort of flow-control for unsolicited status. After unsolicited status is recieved and processed drivers will want to reenable the delivery of unsolicted status by a call to this method.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590454-enableunsolicitedstatus)*