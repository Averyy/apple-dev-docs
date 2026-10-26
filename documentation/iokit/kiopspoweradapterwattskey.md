# kIOPSPowerAdapterWattsKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

This key refers to the wattage of the external AC power adapter attached to a portable. The value associated with this key is a CFNumberRef kCFNumberIntType integer value, in units of watts.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSPowerAdapterWattsKey
```

#### Discussion

This key may be present in the dictionary returned from [`IOPSCopyExternalPowerAdapterDetails`](./api-1523866-iopscopyexternalpoweradapterdeta.md) This key might not be defined in the adapter details dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopspoweradapterwattskey)*