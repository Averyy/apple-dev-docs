# gestaltHasSCC

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltHasSCC = 4
```

## Discussion

The `gestaltHasSCC` bit is normally returned as 0 on the Macintosh IIfx and Macintosh Quadra 900 computers, which have intelligent I/O processors that isolate the hardware and make direct access to the SCC impossible. However, if the user has used the Compatibility Switch control panel to enable compatibility mode, `gestaltHasSCC` is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472318-hardware_attribute_attribute_sel/gestalthasscc)*