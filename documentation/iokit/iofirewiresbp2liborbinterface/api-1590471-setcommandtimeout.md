# setCommandTimeout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the timeout of the ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setCommandTimeout)(void *self, UInt32 timeout);
```

## Discussion

This sets the timeout for the ORB in milliseconds. Note that ORBs without timeouts can be "lost." You will obviously not recieve timeout notification for timeouts of zero. But perhaps less obviously you will not recieve orb reset notification, which is really a sort of accelerated timeout notification for bus reset situations.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.
- `timeout`: The timeout duration in milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590471-setcommandtimeout)*