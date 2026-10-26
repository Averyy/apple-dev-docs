# setCommandGeneration

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the command generation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setCommandGeneration)(void *self, UInt32 generation);
```

#### Discussion

This sets the bus generation this ORB should be appended in. It is only meaningful when combined with the kFWSBP2CommandCheckGeneration flags above.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.
- `generation`: The bus generation for command execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590423-setcommandgeneration)*