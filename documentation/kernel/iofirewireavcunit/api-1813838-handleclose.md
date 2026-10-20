# handleClose

**Framework**: Kernel  
**Kind**: instm

Overrideable method to control the open / close behaviour of an IOService.

## Declaration

```cpp
virtual void handleClose(
 IOService *forClient, 
 IOOptionBitsoptions );
```

#### Overview

See IOService for discussion.

## Parameters

- `forClient`: Designates the client of the provider requesting the close.
- `options`: Options for the close, may be interpreted by the implementor of handleOpen.

## See Also

### Miscellaneous
- [AVCCommand](./api-1813829-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](./api-1813833-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [handleOpen](./api-1813842-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813847-matchpropertytable.md)
  Matching language support Match on the following properties of the unit: Vendor_ID GUID Unit_Type and available sub-units, match if the device has at least the requested number of a sub-unit type: AVCSubUnit_0 -> AVCSubUnit_1f
- [updateAVCCommandTimeout](./api-1813851-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcunit/1813838-handleclose)*