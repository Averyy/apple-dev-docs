# formWhose

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
formWhose = 'whos'
```

## Discussion

Specifies a container of one or more objects and a test to perform on the objects.

The key data for `formWhose` is specified by a whose descriptor, which is a coerced Apple event record of descriptor type `typeWhoseDescriptor`. The data for a whose descriptor consists of two keyword-specified descriptors with the keywords `keyAEIndex` and `keyAETest`.

See also the description for `formTest`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1572727-anonymous/formwhose)*