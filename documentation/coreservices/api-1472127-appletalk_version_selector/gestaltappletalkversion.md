# gestaltAppleTalkVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltAppleTalkVersion = 'atlk'
```

#### Discussion

The version number of the AppleTalk driver (in particular, the .MPP driver) currently installed.   The version number is placed into the low-order byte of the result; ignore the three high-order bytes. If an AppleTalk driver is not currently open, the `response` parameter is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472127-appletalk_version_selector/gestaltappletalkversion)*