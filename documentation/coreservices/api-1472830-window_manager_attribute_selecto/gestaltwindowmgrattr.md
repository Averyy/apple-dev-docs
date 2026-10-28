# gestaltWindowMgrAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltWindowMgrAttr = 'wind'
```

## Discussion

The `Gestalt` selector passed to determine what features of the Window Manager are present. This selector is available with Mac OS 8.5 and later. The `Gestalt` function produces a 32-bit value whose bits you should test to determine which Window Manager features are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472830-window_manager_attribute_selecto/gestaltwindowmgrattr)*