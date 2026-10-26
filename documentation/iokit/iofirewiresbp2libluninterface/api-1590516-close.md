# close

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Opens a connection to a device that is not already open.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*close)(void *self);
```

#### Discussion

Closes an exclusive access to the device. When a device is closed it may be unloaded by the kernel. If it is unloaded and then later reappears it will be represented by a different object. You won't be able to use this user client on the new object. The new object will have to be looked up in the IORegistry and a new user client will have to be opened on it.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLUNInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libluninterface/1590516-close)*