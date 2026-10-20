# UCTypeSelectCreateSelector(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func UCTypeSelectCreateSelector(_ locale: LocaleRef!, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ newSelector: UnsafeMutablePointer<UCTypeSelectRef?>!) -> OSStatus
```

```c
OSStatus UCTypeSelectCreateSelector(LocaleRef locale, LocaleOperationVariant opVariant, UCCollateOptions options, UCTypeSelectRef *newSelector);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390445-uctypeselectcreateselector)*