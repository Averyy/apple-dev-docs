# IODisplayMatchDictionaries

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Match two display information dictionaries to see if they are for the same display.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
SInt32 IODisplayMatchDictionaries(CFDictionaryRef matching1, CFDictionaryRef matching2, IOOptionBits options);
```

#### Return Value

Returns FALSE if the two displays are not equivalent or TRUE if they are.

#### Discussion

By comparing two CFDictionaries returned from IODisplayCreateInfoDictionary(), this function determines if the displays are the same. The information compared is what is returned by calling IODisplayCreateInfoDictionary() with an option of kIODisplayMatchingInfo. This includes information such as the vendor, product, and serial number.

## Parameters

- `matching1`: A CFDictionary returned from IODisplayCreateInfoDictionary().
- `matching2`: Another CFDictionary returned from IODisplayCreateInfoDictionary().
- `options`: No options are currently defined.

## See Also

### Miscellaneous
- [IOCreateDisplayInfoDictionary](./iocreatedisplayinfodictionary.md)
- [IODisplayCreateInfoDictionary](./api-1574917-iodisplaycreateinfodictionary.md)
  Create a CFDictionary with information about display hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1574879-iodisplaymatchdictionaries)*