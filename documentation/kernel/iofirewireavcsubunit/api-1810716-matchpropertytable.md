# matchPropertyTable

**Framework**: Kernel  
**Kind**: instm

Matching language support Match on the following properties of the sub unit: Vendor_ID GUID SubUnit_Type

## Declaration

```swift
virtual bool matchPropertyTable(
 OSDictionary *table);
```

## See Also

- [AVCCommand](iofirewireavcsubunit/1810566-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](iofirewireavcsubunit/1810598-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [handleClose](iofirewireavcsubunit/1810634-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewireavcsubunit/1810680-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [updateAVCCommandTimeout](iofirewireavcsubunit/1810751-updateavccommandtimeout.md)
  By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcsubunit/1810716-matchpropertytable)*