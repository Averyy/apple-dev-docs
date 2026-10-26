# IOGraphicsLib.h

**Framework**: IOKit  
**Role**: API Collection

#### Overview

IOGraphicsLib implements non-kernel task access to IOGraphics family object types - IOFramebuffer and IOAccelerator. These functions implement a graphics family specific API.

A connection to a graphics IOService must be made before these functions are called. A connection is made with the IOServiceOpen() function described in IOKitLib.h. An io_connect_t handle is returned by IOServiceOpen(), which must be passed to the IOGraphicsLib functions. The appropriate connection type from IOGraphicsTypes.h must be specified in the call to IOServiceOpen(). All of the IOFramebuffer functions can only be called from a kIOFBServerConnectType connection. Except as specified below, functions whose names begin with IOFB are IOFramebuffer functions. Functions whose names begin with IOPS are IOAccelerator functions and must be called from connections of type kIOFBEngineControllerConnectType or kIOFBEngineConnectType.

The functions in IOGraphicsLib use a number of special types. The display mode is the screen's resolution and refresh rate. The known display modes are referred to by an index of type IODisplayModeID. The display depth is the number of significant color bits used in representing each pixel. Depths are also referred to by an index value that is 0 for 8 bits, 1 for 15 bits, and 2 for 24 bits. A combination of display mode and depth may have a number of supported pixel formats. The pixel aperture is an index of supported pixel formats for a display mode and depth. This index is of type IOPixelAperture. All of these graphics specific types are defined in IOGraphicsTypes.h.

##### Included Headers

- <IOKit/IOKitLib.h>
- <IOKit/graphics/IOFramebufferShared.h>
- <IOKit/graphics/IOGraphicsInterface.h>

## Topics

### Miscellaneous
- [IOCreateDisplayInfoDictionary](./iocreatedisplayinfodictionary.md)
- [IODisplayCreateInfoDictionary](./api-1574917-iodisplaycreateinfodictionary.md)
  Create a CFDictionary with information about display hardware.
- [IODisplayMatchDictionaries](./api-1574879-iodisplaymatchdictionaries.md)
  Match two display information dictionaries to see if they are for the same display.
### Constants
- [IODisplayDictionaryOptions](./api-1574851-iodisplaydictionaryoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iographicslib_h)*