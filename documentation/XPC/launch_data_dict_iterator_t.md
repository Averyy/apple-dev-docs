# launch_data_dict_iterator_t

**Framework**: XPC  
**Kind**: typealias  
**Role**: Type Alias

A type for iterating over a launch data dictionary.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
typedef void (*)(struct _launch_data *, const char *, void *) launch_data_dict_iterator_t;
```

## See Also

### Data types
- [launch_data_t](./launch_data_t.md)
  A type that represents launch data.
- [launch_data_type_t](./launch_data_type_t.md)
  A type that represents possible types of launch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/launch_data_dict_iterator_t)*