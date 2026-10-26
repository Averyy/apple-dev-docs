# componentFlags

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

A 32-bit field that provides additional information about a particular component.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
UInt32 componentFlags;
```

#### Discussion

The high-order 8 bits are reserved for definition by the Component Manager. If you are developing an application, you should usually set these bits to `0`.

The low-order 24 bits are specific to each component type. These flags can be used to indicate the presence of features or capabilities in a given component.

If you are developing an application that uses components, you can use these flags to further narrow the search criteria applied by the [`FindNextComponent`](../api-1516552-findnextcomponent.md) or [`CountComponents`](../api-1516515-countcomponents.md) function. If you use the [`componentFlags`](./api-1516652-componentflags.md) field in a component search, you use the [`componentFlagsMask`](./api-1516402-componentflagsmask.md) field to indicate which flags are to be considered in the search.

If you are developing a component, you can use these flags to indicate any special capabilities or features of your component. You may use all 24 bits, as appropriate to its component type. You must set all unused bits to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/componentdescription/1516652-componentflags)*