# MDQuerySetCreateValueFunction(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Sets the function used to create the value objects of the MDQuery.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ func: MDQueryCreateValueFunction!, _ context: UnsafeMutableRawPointer!, _ cb: UnsafePointer<CFArrayCallBacks>!)
```

#### Discussion

Values created after a create function is set will be created using the newly specified function, but existing values are not modified. It is not advisable to change this function after `MDQueryExecute` has been called with the query.

## Parameters

- `query`: The query.
- `func`: The callback function the MDQuery should use to create the value list values, such as those returned by the function  . This parameter may be  , in which case any previous value creation settings are cancelled and the MDQuery will subsequently produce the default CFTypeRefs. If a function is specified and is not of type   or does not behave as a   must, the behavior is undefined.
- `context`: A pointer-sized user-defined value, that is passed as the third parameter to the create function. MDQuery does not use this value, does not retain the context in any way, and requires that the context be valid for the lifetime of the query. If the context is not what is expected by the create function, the behavior is undefined.
- `cb`: A pointer to a CFArrayCallBacks structure initialized with the callbacks for the query to use to manage the created value objects. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in, or can be reused for multiple query creations. Only version 0 of the   is supported. The retain field may be  , in which case the MDQuery will not add a retain to the created values. The release field may be  , in which case the MDQuery will do nothing to remove the query's retain (such as the one it gets from the create function) on the value objects when the query is destroyed. If the   field is  , the query will create a simple description for the value objects. If the   field is  , the query will use pointer equality to test for equality of values. This callbacks parameter itself may be   in which case it is treated as a valid version 0 structure with all fields  . Otherwise, if any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a   callbacks structure, the behavior is undefined. If any of the value values returned from the create function is not one understood by one or more of the callback functions, the behavior when those callback functions are used is undefined. For example, if the create function can return  , then   must be understood by the callback functions as a possible parameter. The retain and release callbacks must be a matched set, you should not assume that the retain function will be unused or that additional reference counts will not be taken on the created results.

## See Also

- [func MDQuerySetCreateResultFunction(MDQuery!, MDQueryCreateResultFunction!, UnsafeMutableRawPointer!, UnsafePointer<CFArrayCallBacks>!)](1413064-mdquerysetcreateresultfunction.md)
  Sets the function used to create the result objects of the MDQuery.
- [func MDQuerySetSortComparator(MDQuery!, MDQuerySortComparatorFunction!, UnsafeMutableRawPointer!)](1413087-mdquerysetsortcomparator.md)
  Sets the function used to sort the results of an MDQuery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413017-mdquerysetcreatevaluefunction)*