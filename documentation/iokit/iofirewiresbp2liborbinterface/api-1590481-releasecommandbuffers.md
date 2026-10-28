# releaseCommandBuffers

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Releases SBP2's reference to the command buffers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*releaseCommandBuffers)(void *self);
```

## Return Value

Returns KIOReturnSuccess if the page table was cleared successfully.

## Discussion

When you create a page table with one of the variants of setCommandBuffers. SBP2 holds on to a reference to the buffers until this method is called. This means that if a command completed and you released the buffers without calling this method you could leave FW in an inconsistent state.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590481-releasecommandbuffers)*