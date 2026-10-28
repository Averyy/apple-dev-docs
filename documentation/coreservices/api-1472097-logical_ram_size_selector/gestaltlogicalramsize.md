# gestaltLogicalRAMSize

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltLogicalRAMSize = 'lram'
```

## Discussion

The amount of logical memory available. This value is the same as that returned by `gestaltPhysicalRAMSize` when virtual memory is not installed. On some machines, however, this value might be less than the value returned by `gestaltPhysicalRAMSize` because some RAM may be used by the video display and the Operating System.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472097-logical_ram_size_selector/gestaltlogicalramsize)*