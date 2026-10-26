# updateAVCCommandTimeout

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Updates an AVCCommand's timeout back to 10 seconds.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*updateAVCCommandTimeout)(void *self);
```

#### Discussion

AVCCommands will time out after 10 seconds unless this function is called (from another thread) to update the command's timeout back to 10 seconds. This function is only available if the interface version is > 2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508764-updateavccommandtimeout)*