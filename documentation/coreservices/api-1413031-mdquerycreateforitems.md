# MDQueryCreateForItems(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.7+

## Declaration

```swift
func MDQueryCreateForItems(_ allocator: CFAllocator!, _ queryString: CFString!, _ valueListAttrs: CFArray!, _ sortingAttrs: CFArray!, _ items: CFArray!) -> MDQuery!
```

```c
MDQueryRef MDQueryCreateForItems(CFAllocatorRef allocator, CFStringRef queryString, CFArrayRef valueListAttrs, CFArrayRef sortingAttrs, CFArrayRef items);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1413031-mdquerycreateforitems)*