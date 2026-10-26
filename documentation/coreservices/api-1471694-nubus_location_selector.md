# NuBus Location Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies information about the NuBus slot connector locations.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltNuBusConnectors](./api-1471694-nubus_location_selector/gestaltnubusconnectors.md)
  A bitmap that describes the NuBus slot connector locations. On a Macintosh II, for example, the return value would have bits 9 through 14 set, indicating that 6 NuBus slots are present, at locations 9 through 14.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471694-nubus_location_selector)*