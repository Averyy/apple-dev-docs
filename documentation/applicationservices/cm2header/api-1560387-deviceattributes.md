# deviceAttributes

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

Attributes that are unique to this particular device setup, such as media, paper, and ink types. The data type for this field is an array of two unsigned longs. The low word of `deviceAttributes[0]` is reserved by the ICC. The high word of `deviceAttributes[0]` and the entire word of `deviceAttributes[1]` are available for vendor use. For information on how the bits in `deviceAttributes` are defined and how your application can set and test them, see [Device Attribute Values for Version 2.x Profiles](../api-1560447-x_profiles.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
UInt32 deviceAttributes[2];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cm2header/1560387-deviceattributes)*