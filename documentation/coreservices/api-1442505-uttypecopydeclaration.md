# UTTypeCopyDeclaration(_:)

**Framework**: Core Services  
**Kind**: func

Returns a uniform type’s declaration.

**Availability**:
- iOS 3.0+ - Deprecated in 15.0
- iPadOS 3.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.3+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

## Declaration

```swift
func UTTypeCopyDeclaration(_ inUTI: CFString) -> Unmanaged<CFDictionary>?
```

#### Return_value

A dictionary that contains the uniform type’s declaration, or `NULL` if no declaration for that type can be found.

#### Discussion

A uniform type identifier is declared in a bundle’s information [`Property list`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) (`info.plist`). This function extracts and returns a dictionary that contains the complete declaration of the uniform type identifier. This is useful when your application needs to access properties that does not have a built-in accessor function. For more information on the dictionary format, see [`Uniform Type Identifiers Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## Parameters

- `inUTI`: A uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442505-uttypecopydeclaration)*