# LSSetItemAttribute(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+ - Deprecated in 10.10

## Declaration

```swift
func LSSetItemAttribute(_ inItem: UnsafePointer<FSRef>!, _ inRoles: LSRolesMask, _ inAttributeName: CFString!, _ inValue: CFTypeRef!) -> OSStatus
```

```c
OSStatus LSSetItemAttribute(const FSRef *inItem, LSRolesMask inRoles, CFStringRef inAttributeName, CFTypeRef inValue);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1446733-lssetitemattribute)*