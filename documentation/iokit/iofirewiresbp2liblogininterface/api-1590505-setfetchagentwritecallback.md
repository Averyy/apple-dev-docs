# setFetchAgentWriteCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the callback to be called when the fetch agent write completes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setFetchAgentWriteCallback)(void *self, void *refCon, IOFWSBP2FetchAgentWriteCallback callback);
```

## Discussion

When an immediate orb is executed with submitORB, it's address is written to a specific address on the device. This address is called the fetch agent. The device the reads that orb from the Mac's memory and executes it. With this call you can register to be called back when this write to the fetch agent completes. The SBP2 services guarantee that the fetch agent write will be complete before status is reported for an ORB, so for most drivers this notification is not required.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `refCon`: refCon passed to callback.
- `callback`: address of callback method of type FWSBP2FetchAgentWriteCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590505-setfetchagentwritecallback)*