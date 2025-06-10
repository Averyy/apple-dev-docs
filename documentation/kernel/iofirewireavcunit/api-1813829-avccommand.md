# AVCCommand

**Framework**: Kernel  
**Kind**: instm

Sends an AVC command to the device and stores the response.

## Declaration

```swift
virtual IOReturn AVCCommand(
 const UInt8 *command,
 UInt32cmdLen,
 UInt8 *response,
 UInt32 *responseLen);
```

## Parameters

- `command`: Pointer to command to send.
- `cmdLen`: Length of the command.
- `response`: Pointer to place to store the response.
- `responseLen`: Pointer to response length - initialize to the size of the buffer pointed to by response, updated to the number of bytes returned by the device.

## See Also

- [AVCCommandInGeneration](iofirewireavcunit/1813833-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [handleClose](iofirewireavcunit/1813838-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewireavcunit/1813842-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewireavcunit/1813847-matchpropertytable.md)
  Matching language support Match on the following properties of the unit: Vendor_ID GUID Unit_Type and available sub-units, match if the device has at least the requested number of a sub-unit type: AVCSubUnit_0 -> AVCSubUnit_1f
- [updateAVCCommandTimeout](iofirewireavcunit/1813851-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcunit/1813829-avccommand)*