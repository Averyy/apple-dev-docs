# gestaltROMSize

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltROMSize = 'rom '
```

#### Discussion

The selector you pass to the `Gestalt` function to determine the size of the installed ROM, in bytes. The value is returned in only one word.

You should not infer the existence of certain hardware or software features from the responses that Gestalt returns when you pass it this selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472914-rom_size_selector/gestaltromsize)*