# kIOPSPowerAdapterCurrentKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

This key refers to the current of the external AC power adapter attached to a portable. The value associated with this key is a CFNumberRef kCFNumberIntType integer value, in units of mAmps.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOPSPowerAdapterCurrentKey
```

## Discussion

This key may be present in the dictionary returned from [`IOPSCopyExternalPowerAdapterDetails`](./api-1523866-iopscopyexternalpoweradapterdeta.md) This key might not be defined in the adapter details dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopspoweradaptercurrentkey)*