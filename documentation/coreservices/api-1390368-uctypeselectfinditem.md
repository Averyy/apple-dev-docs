# UCTypeSelectFindItem(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func UCTypeSelectFindItem(_ ref: UCTypeSelectRef!, _ listSize: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ userUPP: IndexToUCStringUPP!, _ closestItem: UnsafeMutablePointer<UInt32>!) -> OSStatus
```

```c
OSStatus UCTypeSelectFindItem(UCTypeSelectRef ref, UInt32 listSize, void *listDataPtr, void *refcon, IndexToUCStringUPP userUPP, UInt32 *closestItem);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390368-uctypeselectfinditem)*