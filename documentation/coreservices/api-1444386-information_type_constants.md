# Information Type Constants

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

The `GetAliasInfo` function uses these constants in the `index` parameter.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [asiZoneName](./api-1444386-information_type_constants/asizonename.md)
  If the record represents a target on an AppleShare volume, retrieve the server’s zone name. Otherwise, return an empty string.
- [asiServerName](./api-1444386-information_type_constants/asiservername.md)
  If the record represents a target on an AppleShare volume, retrieve the server name. Otherwise, return an empty string.
- [asiVolumeName](./api-1444386-information_type_constants/asivolumename.md)
  Return the name of the volume on which the target resides.
- [asiAliasName](./api-1444386-information_type_constants/asialiasname.md)
  Return the name of the target.
- [asiParentName](./api-1444386-information_type_constants/asiparentname.md)
  Return the name of the parent directory of the target of the record. If the target is a volume, return the volume name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444386-information_type_constants)*