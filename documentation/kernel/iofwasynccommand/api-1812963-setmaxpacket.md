# setMaxPacket

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
IOReturn setMaxPacket(
 UInt32maxBytes)
```

#### Overview

Sets the maximum size for block transfers used by the command. The command is initialized to use the maximum packet size calculated from the device's PHY speed, bus info block and the bus topology. Call this method before calling submit().

## Parameters

- `maxBytes`: Maximum packet size in bytes. If the maxsize is 4 then quadlet transfers will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwasynccommand/1812963-setmaxpacket)*