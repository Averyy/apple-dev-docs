# gestaltOSAttr

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltOSAttr = 'os  '
```

## Discussion

The `Gestalt` selector you pass to determine general Operating System attributes, such as whether temporary memory handles are real handles. The low-order bits of the response parameter are interpreted as bit flags. A flag is set to 1 to indicate that the corresponding feature is available. Currently, the following bits are significant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471646-memory_attribute_selectors/gestaltosattr)*