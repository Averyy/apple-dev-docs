# LSIWorkaroundSyncBuffersForOutput

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Synchronize the buffers for output.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*LSIWorkaroundSyncBuffersForOutput)(void *self);
```

## Return Value

Returns kIOReturnSuccess if sync was successful.

## Discussion

Since double buffering may be invovled in the workaround. The driver needs to indicate when these buffers should be syncronized with the original descriptor. For data that will be output LSIWorkaroundSyncBuffersForOutput should be called before submiting the ORB.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590508-lsiworkaroundsyncbuffersforoutpu)*