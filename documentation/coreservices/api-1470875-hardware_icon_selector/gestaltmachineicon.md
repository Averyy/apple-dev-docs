# gestaltMachineIcon

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltMachineIcon = 'micn'
```

#### Discussion

The selector  you pass to the `Gestalt` function to determine the icon family resource ID for the current type of Macintosh.

Never infer the existence of certain hardware or software features from the responses that `Gestalt` returns when you pass it this selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1470875-hardware_icon_selector/gestaltmachineicon)*