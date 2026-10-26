# LSIWorkaroundSyncBuffersForInput

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Synchronize the buffers for input.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*LSIWorkaroundSyncBuffersForInput)(void *self);
```

#### Return Value

Returns kIOReturnSuccess if sync was successful.

#### Discussion

Since double buffering may be invovled in the workaround. The driver needs to indicate when these buffers should be syncronized with the original descriptor. For data that will be input LSIWorkaroundSyncBuffersForInput should be called after receiving completion status for the ORB.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590496-lsiworkaroundsyncbuffersforinput)*