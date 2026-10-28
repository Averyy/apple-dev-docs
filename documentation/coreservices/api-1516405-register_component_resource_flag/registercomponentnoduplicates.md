# registerComponentNoDuplicates

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
registerComponentNoDuplicates = 2
```

## Discussion

Specify this flag to indicate that if a component with identical characteristics to the one being registered already exists, then the new one should not be registered (`RegisterComponent` returns 0 in this situation). If you do not specify this flag, the component is registered even if a component with identical characteristics to the one being registered already exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516405-register_component_resource_flag/registercomponentnoduplicates)*