# componentManufacturer

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

A four-character code that identifies the manufacturer of the component. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
OSType componentManufacturer;
```

## Discussion

The [`componentManufacturer`](./api-1516444-componentmanufacturer.md) field allows for further differentiation between individual components. For example, components made by a specific manufacturer may support an extended feature set. Components provided by Apple use a manufacturer value of `appl`.

If you are developing an application that uses components, you can use this field to find components from a certain manufacturer. Specify the appropriate manufacturer code in this field of the component description structure you supply to the [`FindNextComponent`](../api-1516552-findnextcomponent.md) or [`CountComponents`](../api-1516515-countcomponents.md) function. A value of `0` operates as a wildcard.

If you are developing a component, you obtain your manufacturer code, which can be the same as your application signature, from Apple’s Component Registry Group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentdescription/1516444-componentmanufacturer)*