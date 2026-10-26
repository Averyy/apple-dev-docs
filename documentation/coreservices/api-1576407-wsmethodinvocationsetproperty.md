# WSMethodInvocationSetProperty

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets a named property of the method invocation.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationSetProperty(WSMethodInvocationRef invocation, CFStringRef propertyName, CFTypeRef propertyValue);
```

#### Discussion

Adds properties to a method invocation.  These properties can be user-defined or one of the declared properties, which may alter the behavior of the invocation. Declared properties start with the string "kWS," for example `kWSHTTPFollowsRedirects`. Use these properties to add SOAP action headers or to set debug properties, such as including the raw XML in the method response dictionary. Properties are serialized along with the contract, so you should avoid using raw pointers in a `CFNumber`, for example.

## Parameters

- `invocation`: The method invocation reference.
- `propertyName`: A `CFStringRef` name of the property to set.
- `propertyValue`: A `CFTypeRef` containing the new property value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576407-wsmethodinvocationsetproperty)*