# MDItemGetCacheFileDescriptors(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 15.2+

## Declaration

```swift
func MDItemGetCacheFileDescriptors(_ items: CFArray!, _ completionHandler: ((CFArray?) -> Void)!)
```

```c
void MDItemGetCacheFileDescriptors(CFArrayRef items, void (^completionHandler)(CFArrayRef array));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/4485578-mditemgetcachefiledescriptors)*