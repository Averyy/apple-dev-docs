# updateAVCCommandTimeout

**Framework**: Kernel  
**Kind**: instm

By default, AVCCommands timeout 10 seconds after receiving an Interim response. This function resets the timeout of the current command to 10 seconds from the current time. Call this repeatedly for AVC commands that take a very long time to execute to prevent premature timeout.

## Declaration

```swift
virtual IOReturn updateAVCCommandTimeout() = 0;
```

## See Also

- [AVCCommand](iofirewireavcnub/1810816-avccommand.md)
  Sends an AVC command to the device and stores the response.
- [AVCCommandInGeneration](iofirewireavcnub/1810846-avccommandingeneration.md)
  Sends an AVC command to the device and stores the response. The command must complete in the specified FireWire bus generation otherwise kIOFireWireBusReset is returned.
- [getDevice](iofirewireavcnub/1810878-getdevice.md)
  Returns the FireWire device nub that is this object's provider .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavcnub/1810906-updateavccommandtimeout)*