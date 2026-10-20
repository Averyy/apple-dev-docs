# init(rawValue:)

**Framework**: Video Subscriber Account  
**Kind**: init  
**Role**: Initializer

Creates a new authentication scheme with the specified raw value.

**Availability**:
- iOS
- iPadOS
- macOS
- tvOS
- visionOS

## Declaration

```swift
init(rawValue: String)
```

#### Discussion

This initializer returns `nil` if the raw value you specify doesn’t correspond to a valid authentication scheme type.

## Parameters

- `rawValue`: The raw value to use to create the authentication scheme.

## See Also

### Creating an Authentication Scheme
- [init(String)](./init%28_%29.md)
  Creates a new authentication scheme with the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountproviderauthenticationscheme/init(rawvalue:))*