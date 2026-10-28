# getSessionRef

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the session reference to an already open device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOFireWireSessionRef (*getSessionRef)(void *self);
```

## Return Value

Returns a sessionRef on success.

## Discussion

Sometimes it is desirable to open multiple user clients on a device. In the case of FireWire sometimes we wish to have both the FireWire User Client and the SBP2 User Client open at the same time.

The technique to arbitrate this is as follows:

First open normally the device furthest from the root in the IORegistry.

Second, get its sessionRef with a call to this method.

Third open the device further up the chain by calling openWithSessionRef and passing the sessionRef returned from this call.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590451-getsessionref)*