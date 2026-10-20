# GetIconRefFromFolder(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.15

## Declaration

```swift
func GetIconRefFromFolder(_ vRefNum: Int16, _ parentFolderID: Int32, _ folderID: Int32, _ attributes: Int8, _ accessPrivileges: Int8, _ theIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr
```

```c
OSErr GetIconRefFromFolder(SInt16 vRefNum, SInt32 parentFolderID, SInt32 folderID, SInt8 attributes, SInt8 accessPrivileges, IconRef *theIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1441712-geticonreffromfolder)*