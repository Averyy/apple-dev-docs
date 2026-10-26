# componentSubType

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

A four-character code that identifies the subtype of the component. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
OSType componentSubType;
```

#### Discussion

Different subtypes of a component type may support additional features or provide interfaces that extend beyond the standard functions for a given component type. For example, the subtype of drawing components indicates the type of object the component draws. Drawing components that draw ovals have a subtype of `oval`.

If you are developing an application that uses components, you can use the [`componentSubType`](./api-1516568-componentsubtype.md) field to perform a more specific lookup operation than is possible using only the [`componentType`](./api-1516339-componenttype.md) field. By specifying particular values for both fields in the component description structure that you supply to the [`FindNextComponent`](../api-1516552-findnextcomponent.md) or [`CountComponents`](../api-1516515-countcomponents.md) functions, your application retrieves information about only those components that meet both of these search criteria. A value of `0` operates as a wildcard.

If you are developing a component, you may use this field to indicate more specific information about the capabilities of the component. There are no restrictions on the content you assign to this field. If no additional information is appropriate for your component type, set the [`componentSubType`](./api-1516568-componentsubtype.md) field to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentdescription/1516568-componentsubtype)*