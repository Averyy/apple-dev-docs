# registerComponentGlobal

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
registerComponentGlobal = 1
```

## Discussion

Specify this flag to indicate that this component should be made available to other applications and clients as well as the one performing the registration. If you do not specify this flag, the component is available for use only by the registering application or component (that is, the component is local to the A5 world of the registering program).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516405-register_component_resource_flag/registercomponentglobal)*