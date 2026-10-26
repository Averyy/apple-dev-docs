# openWithSessionRef

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Opens a connection to a device that is already open.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*openWithSessionRef)(void *self, IOFireWireSessionRef sessionRef);
```

#### Return Value

Returns kIOReturnSuccess on success.

#### Discussion

Sometimes it is desirable to open multiple user clients on a device. In the case of FireWire sometimes we wish to have both the FireWire User Client and the SBP2 User Client open at the same time.

The technique to arbitrate this is as follows :

First open normally the device furthest from the root in the IORegistry.

Second, get its sessionRef with the getSessionRef call.

Third open the device further up the chain by calling this method and passing the sessionRef returned from the call in step 2.

## Parameters

- `sessionRef`: SessionRef returned from getSessionRef call.
- `self`: Pointer to IOFireWireSBP2LibLUNInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590563-openwithsessionref)*