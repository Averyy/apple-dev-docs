# AECallObjectAccessor(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Invokes the appropriate object accessor function for a specific desired type and container type. 

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECallObjectAccessor(_ desiredClass: DescType, _ containerToken: UnsafePointer<AEDesc>!, _ containerClass: DescType, _ keyForm: DescType, _ keyData: UnsafePointer<AEDesc>!, _ token: UnsafeMutablePointer<AEDesc>!) -> OSErr
```

```c
OSErr AECallObjectAccessor(DescType desiredClass, const AEDesc *containerToken, DescType containerClass, DescType keyForm, const AEDesc *keyData, AEDesc *token);
```

#### Return Value

A result code. See [Result Codes](../applicationservices/apple_event_manager.md#1656145). `AECallObjectAccessor` returns any result codes returned by the object accessor function it calls.

#### Discussion

If you want your application to do some of the Apple event object resolution normally performed by the [`AEResolve(_:_:_:)`](./api-1449720-aeresolve.md) function, you can use `AECallObjectAccessor` to invoke an object accessor function. This might be useful, for example, if you have installed an object accessor function using `typeWildCard` for the `AEInstallObjectAccessor` function’s `desiredClass` parameter and `typeAEList` for the `containerType` parameter. To return a list of tokens for a request like “line one of every window” the object accessor function can create an empty list, then call `AECallObjectAccessor` for each requested element, adding tokens for each element to the list one at a time.

The parameters of `AECallObjectAccessor` are identical to the parameters of an object accessor function, as described in [`OSLAccessorProcPtr`](./oslaccessorprocptr.md) with one exception—the Apple Event Manager adds a reference constant parameter each time it calls the object accessor function.

You can also call a specific object accessor function directly through its universal procedure pointer with one of the invoke functions described in [Creating, Calling, and Deleting Universal Procedure Pointers](../applicationservices/apple_event_manager.md#1651592). 

##### Version-Notes

In macOS, your application can not make an object callback function available to other applications by installing it in a system object accessor dispatch table.

## Parameters

- `desiredClass`: The type of the Apple event object requested. Some possible values are defined in [Object Class ID Constants](./apple_events/api-1556368-object_class_id_constants.md). See [`DescType`](./desctype.md).
- `containerToken`: A pointer to the token that identifies the container for the desired object. (Token is defined in [`AEDisposeToken(_:)`](./api-1446783-aedisposetoken.md).) See [`AEDesc`](./aedesc.md).
- `containerClass`: The object class of the container for the desired objects. See [`DescType`](./desctype.md).
- `keyForm`: The key form that specifies how to find the object within the container. Key form constants are described in [Key Form and Descriptor Type Object Specifier Constants](./apple_events/api-1572731-key_form_and_descriptor_type_obj.md). See [`DescType`](./desctype.md).
- `keyData`: A pointer to the key data that identifies the object within the container. The type of this data is form-specific. That is, `formName` typically has key data of type `typeText`. See [`AEDesc`](./aedesc.md).
- `token`: A pointer to a token. On return, a token specifying the desired object (or objects). Your application should dispose of this token when it is through with it by calling [`AEDisposeToken(_:)`](./api-1446783-aedisposetoken.md). See [`AEDesc`](./aedesc.md).

## See Also

### Getting, Calling, and Removing Object Accessor Functions
- [func AEGetObjectAccessor(DescType, DescType, UnsafeMutablePointer<OSLAccessorUPP?>!, UnsafeMutablePointer<SRefCon?>!, Bool) -> OSErr](./api-1449054-aegetobjectaccessor.md)
  Gets an object accessor function from an object accessor dispatch table. 
- [func AEInstallObjectAccessor(DescType, DescType, OSLAccessorUPP!, SRefCon!, Bool) -> OSErr](./api-1447905-aeinstallobjectaccessor.md)
  Adds or replaces an entry for an object accessor function to an object accessor dispatch table.
- [func AERemoveObjectAccessor(DescType, DescType, OSLAccessorUPP!, Bool) -> OSErr](./api-1442552-aeremoveobjectaccessor.md)
  Removes an object accessor function from an object accessor dispatch table. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447059-aecallobjectaccessor)*