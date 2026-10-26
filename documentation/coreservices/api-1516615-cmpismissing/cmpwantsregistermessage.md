# cmpWantsRegisterMessage

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The setting of the `cmpWantsRegisterMessage` bit determines whether the Component Manager calls this component during registration. Set this bit to 1 if your component should be called when it is registered; otherwise, set this bit to 0.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
cmpWantsRegisterMessage = 1UL << 31
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516615-cmpismissing/cmpwantsregistermessage)*