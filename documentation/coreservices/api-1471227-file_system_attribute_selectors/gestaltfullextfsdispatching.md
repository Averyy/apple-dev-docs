# gestaltFullExtFSDispatching

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltFullExtFSDispatching = 0
```

## Discussion

If this bit is set in the `response` parameter, all of the functions selected through the `_HFSDispatch` trap are available to external file systems. If this bit is clear, the File Manager checks the selector passed to `_HFSDispatch` and ensures that it is valid; if the selector is invalid, the result code `paramErr` is returned to the caller. If this bit is set, no such validity checking is performed. See the *Guide to the File System Manager* for more information on external file systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471227-file_system_attribute_selectors/gestaltfullextfsdispatching)*