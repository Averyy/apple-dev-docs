# componentType

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

A four-character code that identifies the type of component. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
OSType componentType;
```

## Discussion

All components of a particular type must support a common set of interface functions. For example, drawing components all have a component type of `draw`.

If you are developing an application that uses components, you can use this field to search for components of a given type by specifying the component type in this field of the component description structure you supply to the [`FindNextComponent`](../api-1516552-findnextcomponent.md) function or the [`CountComponents`](../api-1516515-countcomponents.md) function. A value of `0` operates as a wildcard.

If you are developing a component, it must support all of the standard functions for the component type specified by this field. Type codes with all lowercase characters are reserved for definition by Apple. You can define your own component type code as long as you register it with Apple’s Component Registry Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentdescription/1516339-componenttype)*