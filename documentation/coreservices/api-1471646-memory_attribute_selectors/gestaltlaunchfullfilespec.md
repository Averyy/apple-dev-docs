# gestaltLaunchFullFileSpec

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltLaunchFullFileSpec = 2
```

## Discussion

If this bit is set, the `launchControlFlags` field supports control flags in addition to the `launchContinue` flag, and if the `_Launch` trap can process the `launchAppSpec`, `launchProcessSN`, `launchPreferredSize`, `launchMinimumSize`, `launchAvailableSize`, and `launchAppParameters` fields in the launch parameter block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471646-memory_attribute_selectors/gestaltlaunchfullfilespec)*