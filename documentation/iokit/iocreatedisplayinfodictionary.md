# IOCreateDisplayInfoDictionary

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define IOCreateDisplayInfoDictionary(f, o)
```

#### Discussion

IOCreateDisplayInfoDictionary() was renamed IODisplayCreateInfoDictionary(). IOCreateDisplayInfoDictionary() is now a macro for IODisplayCreateInfoDictionary() for compatibility with older code.

## See Also

### Miscellaneous
- [IODisplayCreateInfoDictionary](./api-1574917-iodisplaycreateinfodictionary.md)
  Create a CFDictionary with information about display hardware.
- [IODisplayMatchDictionaries](./api-1574879-iodisplaymatchdictionaries.md)
  Match two display information dictionaries to see if they are for the same display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iocreatedisplayinfodictionary)*