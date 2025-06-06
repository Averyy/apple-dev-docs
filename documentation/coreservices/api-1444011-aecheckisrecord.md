# AECheckIsRecord(_:)

**Framework**: Core Services  
**Kind**: func

Determines whether a descriptor is truly an `AERecord`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func AECheckIsRecord(_ theDesc: UnsafePointer<AEDesc>!) -> Bool
```

#### Return_value

Returns `true` if the descriptor is an `AERecord` or an `AppleEvent`, `false` otherwise.

#### Discussion

Thread safe starting in OS X v10.2.

## Parameters

- `theDesc`: A pointer to the descriptor to check.

## See Also

- [func AEInitializeDesc(UnsafeMutablePointer<AEDesc>!)](1446047-aeinitializedesc.md)
  Initializes a new descriptor. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444011-aecheckisrecord)*