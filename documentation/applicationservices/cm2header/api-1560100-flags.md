# flags

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

Flags that provide hints, such as preferred quality and speed options, to the preferred CMM. The `flags` field consists of an unsigned long data type. The 16 bits in the low word, 0-15, are reserved for use by the ICC. The 16 bits in the high word, 16-31, are available for use by color management systems. For information on how these bits are defined and how your application can set and test them, see [Flag Mask Definitions for Version 2.x Profiles](../api-1560699-x_profiles.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
UInt32 flags;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cm2header/1560100-flags)*