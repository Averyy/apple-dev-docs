# IODisplayCreateInfoDictionary

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Create a CFDictionary with information about display hardware.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
CFDictionaryRef IODisplayCreateInfoDictionary(io_service_t framebuffer, IOOptionBits options);
```

#### Return Value

The returned CFDictionary that should be released by the caller with CFRelease().

#### Discussion

The CFDictionary created by this function contains information about the display hardware associated with a framebuffer. The keys for the dictionary are listed in IOGraphicsTypes.h.

## Parameters

- `framebuffer`: The IOService handle for an IOFramebuffer service.
- `options`: Use IODisplayDictionaryOptions to specify which keys to include.

## See Also

### Miscellaneous
- [IOCreateDisplayInfoDictionary](./iocreatedisplayinfodictionary.md)
- [IODisplayMatchDictionaries](./api-1574879-iodisplaymatchdictionaries.md)
  Match two display information dictionaries to see if they are for the same display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1574917-iodisplaycreateinfodictionary)*