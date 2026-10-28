# formRange

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
formRange = 'rang'
```

## Discussion

Specifies a group of elements between two other elements. The key data is specified by a range descriptor, which is a coerced Apple event record of type `typeRangeDescriptor` that identifies two Apple event objects marking the beginning and end of a range of elements.

The data for a range descriptor consists of two keyword-specified descriptors with the keywords `keyAERangeStart` and `keyAERangeStop`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572731-key_form_and_descriptor_type_obj/formrange)*