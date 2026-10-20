# IOFireWireAVCNub

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

nub for AVC devices

**Availability**:
- macOS 10.2+

## Declaration

```cpp
class IOFireWireAVCNub : IOService
```

#### Overview

## Topics

### Miscellaneous
- [AVCCommand](./iofirewireavcnub/api-1810816-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](./iofirewireavcnub/api-1810846-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [getDevice](./iofirewireavcnub/api-1810878-getdevice.md)
  Returns the FireWire device nub that is this object's provider .
- [updateAVCCommandTimeout](./iofirewireavcnub/api-1810906-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.
### Instance Methods
- [- AVCCommand](./iofirewireavcnub/api-1553103-avccommand.md)
- [- AVCCommandInGeneration](./iofirewireavcnub/api-1553126-avccommandingeneration.md)
- [- getDevice](./iofirewireavcnub/api-1553146-getdevice.md)
- [- getMetaClass](./iofirewireavcnub/api-1553110-getmetaclass.md)
- [- updateAVCCommandTimeout](./iofirewireavcnub/api-1553145-updateavccommandtimeout.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Nubs
- [IOFireWireLocalNode](./iofirewirelocalnode.md)
- [IOFireWireSBP2LUN](./iofirewiresbp2lun.md)
  Provider for most drivers.
- [IOFireWireAVCSubUnit](./iofirewireavcsubunit.md)
  nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.
- [IOFireWireAVCUnit](./iofirewireavcunit.md)
  nub for AVC devices
- [IOFireWireUnit](./iofirewireunit.md)
- [IOFireWireNub](./iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcnub)*