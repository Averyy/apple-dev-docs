# gestaltATalkVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltATalkVersion = 'atkv'
```

#### Discussion

The version number of the AppleTalk driver, in the format introduced with AppleTalk version 56. The version is stored in the high 3 bytes of the return value.

Byte 3 contains the major revision number, byte 2 contains the minor revision number, and byte 1 contains a constant that represents the release stage.

For example, if you call the `Gestalt` function with the 'atkv' selector when AppleTalk version 57 is loaded, you receive the long integer response value $39008000.

Byte 0 always contains 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471416-appletalk_driver_version_selecto/gestaltatalkversion)*