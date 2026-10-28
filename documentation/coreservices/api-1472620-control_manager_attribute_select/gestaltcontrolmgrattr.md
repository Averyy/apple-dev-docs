# gestaltControlMgrAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltControlMgrAttr = 'cntl'
```

## Discussion

The `Gestalt` selector passed to determine what features of the Control Manager are present. This selector is available with Mac OS 8.5 and later. The `Gestalt` function produces a 32-bit value whose bits you should test to determine what Control Manager functionality is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472620-control_manager_attribute_select/gestaltcontrolmgrattr)*